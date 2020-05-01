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

    def __call__(бре):
        бре.и = Словизер(бре.улаз, токен_за_почетак, токен_за_крај)
        т = next(бре.и, токен_за_крај)
        while not крај(т):
            т = бре.линија(т)
        return бре.излаз

    def __str__(бре):
        return ''.join((т.текст for т in бре.излаз))

    def линија(бре, т):
        л = []
        if крај(т):
            return т
        while True:
            if крај(т):
                бре.додај_линију(л)
                return т
            elif неодређен_наводник(т):
                raise Exception('неодређен_наводник', т)
            elif отворени_наводник(т):
                if бре.директан_говор:
                    raise Exception('дупли отворени_наводник', т)
                бре.додај_линију(л)
                бре.директан_говор = True
                return next(бре.и, токен_за_крај)
            elif затворени_наводник(т):
                if not бре.директан_говор:
                    raise Exception('дупли затворени_наводник', т)
                бре.додај_линију(л)
                бре.директан_говор = False
                return next(бре.и, токен_за_крај)
            elif крај_реченице(т) or крај_дела_реченице(т):
                л.append(т)
                бре.додај_линију(л)
                т = next(бре.и, токен_за_крај)
                return т
            else:
                л.append(т)
                т = next(бре.и, токен_за_крај)

    def додај_линију(бре, л):
        # нема нове линије на почетку
        if бре.излаз and not нова_линија(бре.излаз[-1]):
            if л == []:
                # нема нове линије на крају
                return
            бре.излаз.append(ТокенСам('\n'))
        л = трим(л)
        if л == [] and бре.директан_говор:
            # прескочи да не цитирамо празну линију
            return
        if бре.директан_говор:
            бре.излаз.append(ТокенОтворениНаводник('„'))
            бре.излаз.extend(л)
            бре.излаз.append(ТокенЗатворениНаводник('“'))
        else:
            бре.излаз.extend(л)

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

