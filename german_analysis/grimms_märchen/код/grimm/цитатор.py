import re
from grimm.токенизер import ТОКЕН_ЗА_ПОЧЕТАК, ТОКЕН_ЗА_КРАЈ
from grimm.токенизер import ТОКЕН_ЊАК
from grimm.токенизер import ТОКЕН_ОТВОРЕНИ_НАВОДНИК, ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК
from grimm.токенизер import је_реч, је_спејс, је_токен_за_крај, је_токен_за_почетак
from grimm.словизер import Словизер


class ЦитатГрешка(Exception):
    pass


class Цитатор:
    def __init__(бре, улаз):
        бре.улаз = улаз
        бре.излаз = []

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
        else:
            бре.излаз.append(т)

    def __str__(бре):
        return ''.join((т.текст for т in бре.излаз))

    def цитат_грешка(бре, код):
        досад = ''.join([т.текст for т in бре.излаз])
        raise ЦитатГрешка(f"Лош цитат: '{код}', текст={досад[-100:]}")

    def одреди_наводник(бре, код):
        НА_КРАЈУ_ТЕКСТА = ['"џ"^^', ' џ"^^', 'џ."^^']
        # ЗАТВОРЕН_ЦИТАТ = ['џ." џ', 'џ," џ', 'џ."\n"', 'џ?" -', 'џ." -', 'џ."\nџ', 'џ!" џ', 'џ?" џ', 'џ."\n\n']
        ЗАТВОРЕН_ЦИТАТ = re.compile('џ[.,?!]["][ \n][џ"\n-]')
        затворени = []
        затворени.extend(НА_КРАЈУ_ТЕКСТА)
        # затворени.extend(ЗАТВОРЕН_ЦИТАТ)

        НА_ПОЧЕТКУ_ТЕКСТА = ['^^"џ ']
        НАКОН_ДВОТАЧКЕ = [': "џ"', ': "џ ']
        НАКОН_ЗАРЕЗА = [', "џ ']
        НАКОН_ЦРТЕ = ['- "џ,', '- "џ ']
        НАКОН_ТАЧКЕ = ['. "џ ', '. "џ,']
        НОВА_ЛИНИЈА = [':\n"џ,', '"\n"џ ']
        отворени = []
        отворени.extend(НА_ПОЧЕТКУ_ТЕКСТА)
        отворени.extend(НАКОН_ДВОТАЧКЕ)
        отворени.extend(НАКОН_ЗАРЕЗА)
        отворени.extend(НАКОН_ЦРТЕ)
        отворени.extend(НАКОН_ТАЧКЕ)
        отворени.extend(НОВА_ЛИНИЈА)

        if код in отворени:
            return ТОКЕН_ОТВОРЕНИ_НАВОДНИК
        if код in НА_КРАЈУ_ТЕКСТА:
            return ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК
        if ЗАТВОРЕН_ЦИТАТ.fullmatch(код):
            return ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК
        return None

    def наводник(бре):
        def код(т):
            БИТНИ_СИМБОЛИ = [':', '"', '.', '?', '!', ',', '-', '\n']
            НЕБИТНИ_СИМБОЛИ = ['^', '$', '\'']
            if т.текст in БИТНИ_СИМБОЛИ:
                return т.текст
            if т.текст in НЕБИТНИ_СИМБОЛИ:
                return '#'
            if је_спејс(т):
                return ' '
            if је_реч(т):
                return 'џ'
            if је_токен_за_почетак(т):
                return '^'
            if је_токен_за_крај(т):
                return '$'
            raise Exception('непознато', т)
        к = код(бре.и.пре_два) + код(бре.и.претходно) + код(бре.и.тренутно) + код(бре.и.следеће) + код(бре.и.за_два)
        н = бре.одреди_наводник(к)
        if н:
            return н
        бре.цитат_грешка(к)

