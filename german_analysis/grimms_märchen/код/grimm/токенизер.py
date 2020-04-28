import re
import sys
from collections import namedtuple
КРАЈ = '<<крај>>'
ТокенЗаКрај = namedtuple('ТокенЗаКрај', ['текст'])
ТокенРеч = namedtuple('ТокенРеч', ['текст'])
ТокенСпејс = namedtuple('ТокенСпејс', ['текст'])
ТокенСам = namedtuple('ТокенСам', ['текст'])
СЛОВА = re.compile('[a-zA-Zßäöü]')
СЕПАРАТОРИ = re.compile(r'[.,:;"\'!?-]')


class Токенизер():
    def __init__(бре, текст):
        бре.текст = текст
        бре.токени = []

    def __call__(бре):
        бре.и = iter(бре.текст)
        бре.израз(next(бре.и, КРАЈ))

    def израз(бре, к):
        if к == КРАЈ:
            бре.токени.append(ТокенЗаКрај(''))
        elif СЛОВА.fullmatch(к):
            бре.реч(к)
        elif к == ' ':
            бре.спејс(к)
        elif к == '\n' or СЕПАРАТОРИ.fullmatch(к):
            бре.сам(к)
        else:
            raise Exception(f'Непознато слово: "{к}"')

    def реч(бре, к):
        текст = к
        к = next(бре.и, КРАЈ)
        while СЛОВА.fullmatch(к):
            текст += к
            к = next(бре.и, КРАЈ)
        бре.токени.append(ТокенРеч(текст))
        бре.израз(к)

    def спејс(бре, к):
        текст = к
        к = next(бре.и, КРАЈ)
        while к == ' ':
            текст += к
            к = next(бре.и, КРАЈ)
        бре.токени.append(ТокенСпејс(текст))
        бре.израз(к)

    def сам(бре, к):
        бре.токени.append(ТокенСам(к))
        бре.израз(next(бре.и, КРАЈ))


def главна():
    with open('/tmp/www.grimmstories.com/1/ff4eb3599fcbe363a89a9553dfef5385840ec239afbd4d9c604db23c5b3b837c', 'r') as ф:
        ток = Токенизер(ф.read())
        ток()


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    главна()

