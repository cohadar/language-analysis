import re
from grimm.токенизер import ТОКЕН_ЗА_ПОЧЕТАК, ТОКЕН_ЗА_КРАЈ
from grimm.токенизер import ТОКЕН_ЊАК
from grimm.токенизер import ТОКЕН_ОТВОРЕНИ_НАВОДНИК, ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК, ТОКЕН_ДУГА_ЦРТА
from grimm.токенизер import је_реч, је_спејс, је_број, је_токен_за_крај, је_токен_за_почетак
from grimm.словизер import Словизер


class ЦитатГрешка(Exception):
    pass


class Цитатор:
    def __init__(бре, улаз):
        бре.улаз = улаз
        бре.излаз = []
        бре.директан_говор = False

    def __call__(бре):
        бре.директан_говор = False
        бре.и = Словизер(бре.улаз, почетак=ТОКЕН_ЗА_ПОЧЕТАК, крај=ТОКЕН_ЗА_КРАЈ)
        next(бре.и, ТОКЕН_ЗА_КРАЈ)
        while not је_токен_за_крај(бре.и.тренутно):
            бре.цитирај()
            next(бре.и, ТОКЕН_ЗА_КРАЈ)
        return бре.излаз

    def цитирај(бре):
        т = бре.и.тренутно
        if т.текст == '"':
            бре.излаз.append(бре.наводник())
        elif т.текст == '-':
            бре.излаз.append(бре.црта())
        else:
            бре.излаз.append(т)

    def __str__(бре):
        return ''.join((т.текст for т in бре.излаз))

    def цитат_грешка(бре, код, порука):
        досад = ''.join([т.текст for т in бре.излаз])
        return ЦитатГрешка(код, порука, f"текст={досад[-100:]}")

    def отворени_наводник(бре, код):
        отворени_кодови = []
        отворени_кодови.append(re.compile('[-,.;:џ–] "џ '))
        отворени_кодови.append(re.compile('[-,.?:џ–] "џ,'))
        отворени_кодови.append(re.compile('[-,.:џ] "џ!'))
        отворени_кодови.append(re.compile('[-] "џ.'))
        отворени_кодови.append(re.compile('[.] "џ?'))
        отворени_кодови.append(re.compile('[,] "џ!'))
        отворени_кодови.append(re.compile('[:] "џ\''))
        отворени_кодови.append(re.compile('[".:\n]\n"џ '))
        отворени_кодови.append(re.compile('[".:\n]\n"џ,'))
        отворени_кодови.append(re.compile('["]\n"џ!'))
        отворени_кодови.append(re.compile('[:,] " џ'))
        отворени_кодови.append(re.compile(' [-]"џ,'))
        отворени_кодови.append(re.compile(' [-]"џ '))
        отворени_кодови.append(re.compile(' ."џ '))
        отворени_кодови.append(re.compile('џ:"џ '))
        отворени_кодови.append(re.compile('џ:" џ'))
        отворени_кодови.append(re.compile(': "џ.'))
        отворени_кодови.append(re.compile(': "џ '))
        ЂУБРЕ = '[.,;?!\nџ)][ \n]"џ[.,? "]'
        отворени_кодови.append(re.compile(ЂУБРЕ))
        for ок in отворени_кодови:
            if ок.fullmatch(код):
                return ТОКЕН_ОТВОРЕНИ_НАВОДНИК
        return None

    def затворени_наводник(бре, код):
        затворени_кодови = []
        затворени_кодови.append(re.compile('џ[.!?,; ]" џ'))
        затворени_кодови.append(re.compile('џ[.!?]" -'))
        затворени_кодови.append(re.compile('џ[.!?]" –'))
        затворени_кодови.append(re.compile('џ[.!?]" \n'))
        затворени_кодови.append(re.compile('џ[.!?,]"\nџ'))
        затворени_кодови.append(re.compile('џ[.!?]"\n\n'))
        затворени_кодови.append(re.compile('џ[.!?]"\n"'))
        затворени_кодови.append(re.compile('[!?]," џ'))
        затворени_кодови.append(re.compile('[ "]џ"; '))
        затворени_кодови.append(re.compile('[ "]џ" џ'))
        затворени_кодови.append(re.compile('[.!] " џ'))
        затворени_кодови.append(re.compile(' џ" [-–]'))
        ЂУБРЕ = '[џ.‹!?\')][.,!‹\']"[ \n][\n-.(џ]'
        затворени_кодови.append(re.compile(ЂУБРЕ))
        for зк in затворени_кодови:
            if зк.fullmatch(код):
                return ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК
        СУМЊИВО_ЗАТВАРАЊЕ = ['џ " џ', 'џ." #']
        if код in СУМЊИВО_ЗАТВАРАЊЕ:
            return ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК
        ЛАЖНО_ЗАТВАРАЊЕ = 'џ:" џ'
        if код == ЛАЖНО_ЗАТВАРАЊЕ:
            return None
        return None

    def наводник(бре):
        к = код(бре.и.пре_два) + код(бре.и.претходно) + код(бре.и.тренутно) + код(бре.и.следеће) + код(бре.и.за_два)
        with open('/tmp/a', 'a') as ф:
            ф.write(к.replace('\n', '\\n') + '\n')
        от = бре.отворени_наводник(к)
        за = бре.затворени_наводник(к)
        if от and за:
            raise бре.цитат_грешка(к, 'немож оба цитата мајсторе')
        if от:
            if бре.директан_говор:
                raise бре.цитат_грешка(к, 'дупли отворени цитат')
            бре.директан_говор = True
            return от
        if за:
            if not бре.директан_говор:
                raise бре.цитат_грешка(к, 'дупли затворени цитат')
            бре.директан_говор = False
            return за
        raise бре.цитат_грешка(к, 'непознат цитат код')

    def црта(бре):
        if је_спејс(бре.и.претходно) and је_спејс(бре.и.следеће):
            return ТОКЕН_ДУГА_ЦРТА
        if је_спејс(бре.и.претходно) and бре.и.следеће.текст == '"':
            return ТОКЕН_ДУГА_ЦРТА
        return бре.и.тренутно


def код(т):
    БИТНИ_СИМБОЛИ = [':', '"', '„', '“', '.', '?', '!', ',', ';', '-', '–', '\n']
    НЕБИТНИ_СИМБОЛИ = [
        '^', '$', '\'', '(', ')', '[', ']', '=', '‹', '›', '/']
    if т.текст in БИТНИ_СИМБОЛИ:
        return т.текст
    if т.текст in НЕБИТНИ_СИМБОЛИ:
        return т.текст
    if је_спејс(т):
        return ' '
    if је_број(т):
        return '0'
    if је_реч(т):
        return 'џ'
    if је_токен_за_почетак(т):
        return '\n'
    if је_токен_за_крај(т):
        return '\n'
    raise Exception('непознато', т)

