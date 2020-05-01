from grimm.токенизер import ТокенСпејс, ТокенЗаКрај, ТокенСам, ТокенРеч
from grimm.токенизер import ТокенНаводник, ТокенЗатворениНаводник, ТокенОтворениНаводник
from grimm.токенизер import токен_за_почетак, токен_за_крај
from grimm.словизер import Словизер
КРАЈ = ТокенЗаКрај('')


def крај(т):
    return type(т) == ТокенЗаКрај


def неодређен_наводник(т):
    return type(т) == ТокенНаводник


def реч(т):
    return type(т) == ТокенРеч


class Цитатор:
    def __init__(бре, улаз):
        бре.улаз = улаз
        бре.излаз = []

    def __call__(бре):
        бре.и = Словизер(бре.улаз, почетак=токен_за_почетак, крај=токен_за_крај)
        next(бре.и, КРАЈ)
        while not крај(бре.и.тренутно):
            бре.цитирај()
        return бре.излаз

    def цитирај(бре):
        т = бре.и.тренутно
        if неодређен_наводник(т):
            бре.излаз.append(бре.наводник())
        else:
            бре.излаз.append(т)
        next(бре.и, КРАЈ)

    def __str__(бре):
        return ''.join((т.текст for т in бре.излаз))

    def наводник(бре):
        if бре.и.претходно.текст in [' ', '\n', '', ':'] and реч(бре.и.следеће):
            бре.излаз.append(ТокенОтворениНаводник('„'))
        elif бре.и.претходно.текст in [',', ';', '.', '!', '?'] and бре.и.следеће.текст in [' ', '\n', '']:
            бре.излаз.append(ТокенЗатворениНаводник('“'))
        elif реч(бре.и.претходно) and бре.и.следеће.текст in [' ', '\n', '', ';']:
            бре.излаз.append(ТокенЗатворениНаводник('“'))
        # elif бре.и.претходно.текст == ' ' and бре.и.следеће.текст == ' ' and бре.излаз[-2].текст in [',', ';', '.', '
        else:
            if бре.и.тренутно.текст == "'":
                бре.излаз.append(бре.и.тренутно)
            else:
                досад = ''.join([т.текст for т in бре.излаз])
                raise Exception(f'Лош цитат: ({бре.и.тренутно}), линија={бре.и.линија}, текст={досад[-100:]}')
        return next(бре.и, КРАЈ)

