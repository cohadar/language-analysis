from grimm.токенизер import ТокенСпејс, ТокенЗаКрај, ТокенСам, ТокенРеч
from grimm.токенизер import ТокенНаводник, ТокенЗатворениНаводник, ТокенОтворениНаводник
from grimm.токенизер import токен_за_почетак, токен_за_крај
from grimm.словизер import Словизер


def крај(т):
    return type(т) == ТокенЗаКрај


def спејс(т):
    return type(т) == ТокенСпејс


def реч(т):
    return type(т) == ТокенРеч


def крај_реченице(т):
    return т.текст in ['.', '!', '?']


def крај_дела_реченице(т):
    return т.текст in [',', ';', ':']


def нова_линија(т):
    return т.текст == '\n'


def тачка(т):
    return т.текст == '.'


def неодређен_наводник(т):
    return type(т) == ТокенНаводник


def отворени_наводник(т):
    return type(т) == ТокенОтворениНаводник


def затворени_наводник(т):
    return type(т) == ТокенЗатворениНаводник


def јел_наводник(т):
    return неодређен_наводник(т) or отворени_наводник(т) or затворени_наводник(т)


def трим(л):
    if not л:
        return л
    if спејс(л[0]):
        return трим(л[1:])
    if спејс(л[-1]):
        return трим(л[:-1])
    return л


class Линајзер():
    def __init__(бре, улаз):
        def џемирај(т):
            if реч(т):
                return ТокенРеч('џемо') if len(т.текст) > 3 else т
            else:
                return т
        бре.улаз = улаз
        # бре.улаз = [џемирај(т) for т in улаз]
        бре.директан_говор = False
        бре.излаз = []
        бре.последњи_наводник = None

    def __call__(бре):
        бре.и = Словизер(бре.улаз, токен_за_почетак, токен_за_крај)
        т = next(бре.и, токен_за_крај)
        while not крај(т):
            т, л = бре.линија(т)
            бре.излаз.extend(трим(л))
        return бре.излаз

    def __str__(бре):
        return ''.join((т.текст for т in бре.излаз))

    def линија(бре, т):
        л = []
        if крај(т):
            return т, л
        while True:
            if крај(т):
                return т, л
            elif крај_реченице(т):
                л.append(т)
                л.append(ТокенСам('\n'))
                т = next(бре.и, токен_за_крај)
                return т, л
            else:
                л.append(т)
                т = next(бре.и, токен_за_крај)

    # def додај(бре, линија):
    #     assert isinstance(линија, list), линија
    #     if линија == [] and бре.излаз and нова_линија(бре.излаз[-1]):
    #         # прескочи, да не правимо дупле празне линије
    #         return
    #     if линија == [] and бре.директан_говор:
    #         # прескочи да не цитирамо празну линију
    #         return
    #     if бре.директан_говор:
    #         бре.излаз.append(бре.последњи_наводник)
    #         бре.излаз.extend(линија)
    #         бре.излаз.append(бре.последњи_наводник)
    #     else:
    #         бре.излаз.extend(линија)

    # def линија(бре, т):
    #     if крај(т):
    #         return т
    #     л = []
    #     if спејс(т):
    #         т = next(бре.и, КРАЈ)
    #         if крај(т):
    #             бре.излаз.extend(л)
    #             return т
    #     while True:
    #         if јел_наводник(т):
    #             return бре.одреди_наводник(л, т)
    #         if нова_линија(т):
    #             бре.излаз.extend(л)
    #             бре.додај([])
    #             т = next(бре.и, КРАЈ)
    #             return т
    #         elif крај_реченице(т):
    #             л.append(т)
    #             бре.излаз.extend(л)
    #             п = т
    #             т = next(бре.и, КРАЈ)
    #             if бре.директан_говор and тачка(п) and јел_наводник(т):
    #                 бре.излаз.append(ТокенСам('\n', т.индекс))
    #             else:
    #                 бре.додај([])
    #             return т
    #         elif крај_дела_реченице(т):
    #             л.append(т)
    #             бре.излаз.extend(л)
    #             т = next(бре.и, КРАЈ)
    #             return т
    #         elif крај(т):
    #             бре.излаз.extend(л)
    #             return т
    #         else:
    #             л.append(т)
    #             т = next(бре.и, КРАЈ)

    # def одреди_наводник(бре, л, т):
    #     бре.последњи_наводник = т
    #     if бре.директан_говор:
    #         if л != []:
    #             бре.излаз.extend(л)
    #         т = next(бре.и, КРАЈ)
    #         бре.директан_говор = True
    #         return т
    #     else:
    #         бре.излаз.extend(л)
    #         т = next(бре.и, КРАЈ)
    #         бре.директан_говор = False
    #         return т

