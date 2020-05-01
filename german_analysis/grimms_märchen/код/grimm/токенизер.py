import re
from collections import namedtuple
from grimm.словизер import Словизер

_ТокенФиксни = namedtuple('_ТокенФиксни', ['текст'])
ТокенПразан = namedtuple('ТокенЗаКрај', ['текст'])
ТокенРеч = namedtuple('ТокенРеч', ['текст'])
ТокенСпејс = namedtuple('ТокенСпејс', ['текст'])
ТокенСам = namedtuple('ТокенСам', ['текст'])
ТокенНаводник = namedtuple('ТокенНаводник', ['текст'])
ТокенОтворениНаводник = namedtuple('ТокенОтворениНаводник', ['текст'])
ТокенЗатворениНаводник = namedtuple('ТокенЗатворениНаводник', ['текст'])
ТокенСамНеаски = namedtuple('ТокенСамНеаски', ['текст'])
ТокенБрој = namedtuple('ТокенБрој', ['текст'])
ТокенСумњив = namedtuple('ТокенСумњив', ['текст'])


ТОКЕН_ЗА_ПОЧЕТАК = _ТокенФиксни('')
ТОКЕН_ЗА_КРАЈ = _ТокенФиксни('')
ТОКЕН_НОВА_ЛИНИЈА = _ТокенФиксни('\n')


КРАЈ_ТЕКСТ = '<<крај>>'
СЛОВА = re.compile('[a-zA-ZßäöüÄÖÜ]')
СЕПАРАТОРИ = re.compile(r'[=.,:;"\'\(\)\[\]!?\-]')
НЕАСКИ_СЕПАРАТОРИ = re.compile(r'[–‹›]')
ЦИФРЕ = re.compile(r'[0-9]')
СУМЊИВИ = re.compile(r'[\^\/`]')  # највероватније за игнорисати


class Токенизер():
    def __init__(бре, текст):
        бре.текст = текст
        бре.токени = []
        број_дуплих = len([ц for ц in текст if ц == '"'])
        број_обичних = len([ц for ц in текст if ц == "'"])
        бре._наводник = "'" if број_обичних > број_дуплих else '"'

    def __call__(бре):
        бре.и = Словизер(бре.текст, -1, -1)
        бре.израз(next(бре.и, КРАЈ_ТЕКСТ))
        return бре.токени

    def израз(бре, к):
        while к != КРАЈ_ТЕКСТ:
            if к == КРАЈ_ТЕКСТ:
                бре.токени.append(ТОКЕН_ЗА_КРАЈ)
                return
            elif СЛОВА.fullmatch(к):
                к = бре.реч(к)
            elif к == ' ':
                к = бре.спејс(к)
            elif к == '\n' or СЕПАРАТОРИ.fullmatch(к):
                к = бре.сам(к)
            elif НЕАСКИ_СЕПАРАТОРИ.fullmatch(к):
                к = бре.сам_неаски(к)
            elif СУМЊИВИ.fullmatch(к):
                к = бре.сумњив(к)
            elif ЦИФРЕ.fullmatch(к):
                к = бре.број(к)
            else:
                raise Exception(f'Непознато слово: "{к}"')
        бре.токени.append(ТОКЕН_ЗА_КРАЈ)

    def реч(бре, к):
        текст = к
        к = next(бре.и, КРАЈ_ТЕКСТ)
        while СЛОВА.fullmatch(к):
            текст += к
            к = next(бре.и, КРАЈ_ТЕКСТ)
        бре.токени.append(ТокенРеч(текст))
        return к

    def спејс(бре, к):
        текст = к
        к = next(бре.и, КРАЈ_ТЕКСТ)
        while к == ' ':
            текст += к
            к = next(бре.и, КРАЈ_ТЕКСТ)
        бре.токени.append(ТокенСпејс(текст))
        return к

    def сам(бре, к):
        if к == бре._наводник:
            бре.токени.append(ТокенНаводник(к))
        else:
            бре.токени.append(ТокенСам(к))
        return next(бре.и, КРАЈ_ТЕКСТ)

    def сам_неаски(бре, к):
        бре.токени.append(ТокенСамНеаски(к))
        return next(бре.и, КРАЈ_ТЕКСТ)

    def сумњив(бре, к):
        бре.токени.append(ТокенСумњив(к))
        return next(бре.и, КРАЈ_ТЕКСТ)

    def број(бре, к):
        текст = к
        к = next(бре.и, КРАЈ_ТЕКСТ)
        while ЦИФРЕ.fullmatch(к):
            текст += к
            к = next(бре.и, КРАЈ_ТЕКСТ)
        бре.токени.append(ТокенБрој(текст))
        return к

