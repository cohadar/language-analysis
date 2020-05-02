from grimm.токенизер import ТОКЕН_ЗА_ПОЧЕТАК, ТОКЕН_ЗА_КРАЈ, ТОКЕН_НОВА_ЛИНИЈА
from grimm.токенизер import ТОКЕН_ОТВОРЕНИ_НАВОДНИК, ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК, ТОКЕН_ЊАК
from grimm.токенизер import је_спејс, је_неодређени_наводник, је_нова_линија
from grimm.токенизер import је_токен_за_крај
from grimm.токенизер import је_отворени_наводник, је_затворени_наводник
from grimm.словизер import Словизер


def крај_реченице(т):
    return т.текст in ['.', '!', '?']


def крај_дела_реченице(т):
    return т.текст in [',', ';', ':']


def тачка(т):
    return т.текст == '.'


def трим(л):
    if not л:
        return л
    if је_спејс(л[0]):
        return трим(л[1:])
    if је_спејс(л[-1]):
        return трим(л[:-1])
    return л


class Линајзер():
    def __init__(бре, улаз):
        # def џемирај(т):
        #     if је_реч(т):
        #         return _ТокенРеч('џемо') if len(т.текст) > 3 else т
        #     else:
        #         return т
        бре.улаз = улаз
        # бре.улаз = [џемирај(т) for т in улаз]
        бре.директан_говор = False
        бре.излаз = []
        бре.линије = []

    def __call__(бре):
        бре.и = Словизер(бре.улаз, ТОКЕН_ЗА_ПОЧЕТАК, ТОКЕН_ЗА_КРАЈ)
        т = next(бре.и, ТОКЕН_ЗА_КРАЈ)
        while not је_токен_за_крај(т):
            т = бре.линија(т)
        return бре.излаз

    def __str__(бре):
        return ''.join((т.текст for т in бре.излаз))

    def линија(бре, т):
        л = []
        if је_токен_за_крај(т):
            return т
        while True:
            if је_токен_за_крај(т):
                т = бре.додај_прелом(л, бре.директан_говор)
                return т
            if је_неодређени_наводник(т):
                raise Exception('неодређен_наводник', str(бре)[-100:])
            if је_отворени_наводник(т):
                if бре.директан_говор:
                    raise Exception('дупли отворени_наводник', str(бре)[-100:])
                т = бре.додај_прелом(л, False)
                бре.директан_говор = True
                return т
            if је_затворени_наводник(т):
                if not бре.директан_говор:
                    raise Exception('дупли затворени_наводник', str(бре)[-100:])
                т = бре.додај_прелом(л, True)
                бре.директан_говор = False
                return т
            if је_нова_линија(т):
                т = бре.додај(л, бре.директан_говор)
                return т
            if крај_реченице(т) or крај_дела_реченице(т) or је_нова_линија(т):
                л.append(т)
                т = бре.додај_прелом(л, бре.директан_говор)
                return т
            л.append(т)
            т = next(бре.и, ТОКЕН_ЗА_КРАЈ)

    def додај_прелом(бре, л, цитирај):
        л = трим(л)
        if not л:
            return next(бре.и, ТОКЕН_ЗА_КРАЈ)
        прескочи = False
        л2 = []
        if цитирај:
            л2.append(ТОКЕН_ОТВОРЕНИ_НАВОДНИК)
            л2.extend(л)
            л2.append(ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК)
        else:
            л2.extend(л)
        if је_токен_за_крај(бре.и.следеће):
            # прескочи нову линију на крају
            прескочи = True
        if цитирај and је_затворени_наводник(бре.и.следеће):
            прескочи = True
        if not прескочи:
            # л2.append(ТОКЕН_ЊАК)
            л2.append(ТОКЕН_НОВА_ЛИНИЈА)
        бре.излаз.extend(л2)
        бре.линије.append(''.join([т.текст for т in л2]))
        return next(бре.и, ТОКЕН_ЗА_КРАЈ)

    def додај(бре, л, цитирај):
        if not л and бре.излаз and је_нова_линија(бре.излаз[-1]):
            return next(бре.и, ТОКЕН_ЗА_КРАЈ)
        л2 = []
        if цитирај:
            л2.append(ТОКЕН_ОТВОРЕНИ_НАВОДНИК)
            л2.extend(трим(л))
            л2.append(ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК)
        else:
            л2.extend(трим(л))
        # л2.append(ТОКЕН_ЊАК)
        л2.append(ТОКЕН_НОВА_ЛИНИЈА)
        бре.излаз.extend(л2)
        бре.линије.append(''.join([т.текст for т in л2]))
        return next(бре.и, ТОКЕН_ЗА_КРАЈ)

