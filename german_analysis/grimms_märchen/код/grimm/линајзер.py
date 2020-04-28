from grimm.токенизер import ТокенСпејс, ТокенЗаКрај
КРАЈ = ТокенЗаКрај('')


def крај(т):
    return type(т) == ТокенЗаКрај


def спејс(т):
    return type(т) == ТокенСпејс


def крај_реченице(т):
    return т.текст in ['.', '!', '?']


class Линајзер():
    def __init__(бре, токени):
        бре.токени = токени
        бре.линије = []

    def __call__(бре):
        бре.и = iter(бре.токени)
        т = next(бре.и, КРАЈ)
        while not крај(т):
            т = бре.линија(т)
        return бре.линије

    def линија(бре, т):
        if крај(т):
            return т
        л = ""
        if спејс(т):
            т = next(бре.и, КРАЈ)
            if крај(т):
                бре.линије.append(л)
                return т
        while True:
            if т.текст == '"':
                л += т.текст
                т = next(бре.и, КРАЈ)
                т, нл, дп = бре.директан_говор(т)
                л += нл
                if крај_реченице(дп):
                    бре.линије.append(л)
                    return т
            elif т.текст == '\n' or крај_реченице(т):
                if т.текст != '\n':
                    л += т.текст
                бре.линије.append(л)
                т = next(бре.и, КРАЈ)
                return т
            elif крај(т):
                бре.линије.append(л)
                return т
            else:
                л += т.текст
                т = next(бре.и, КРАЈ)

    def директан_говор(бре, т):
        л = ""
        п = КРАЈ
        while True:
            if т.текст == '"':
                л += т.текст
                т = next(бре.и, КРАЈ)
                return т, л, п
            elif крај(т):
                return т, л, п
            else:
                л += т.текст
                п = т
                т = next(бре.и, КРАЈ)

