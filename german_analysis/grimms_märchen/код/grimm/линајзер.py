from grimm.токенизер import ТокенСпејс, ТокенЗаКрај, ТокенСам, ТокенРеч
КРАЈ = ТокенЗаКрај('')


def крај(т):
    return type(т) == ТокенЗаКрај


def спејс(т):
    return type(т) == ТокенСпејс


def реч(т):
    return type(т) == ТокенРеч


def крај_реченице(т):
    return т.текст in ['.', '!', '?']


def крај_дела_реченице(т):
    return т.текст in [',', ';']


class Линајзер():
    def __init__(бре, токени):
        def дуплирај(т):
            if т.текст == "'":
                return ТокенСам('"')
            else:
                return т

        def џемирај(т):
            if реч(т):
                return ТокенРеч('џемо') if len(т.текст) > 3 else т
            else:
                return т
        бре.линије = []
        бре.токени = токени
        # бре.токени = [џемирај(т) for т in токени]
        број_дуплих = len([т for т in токени if т.текст == '"'])
        број_обичних = len([т for т in токени if т.текст == "'"])
        бре.наводник = "'" if број_обичних > број_дуплих else '"'
        if број_дуплих == 0:
            бре.наводник = '"'
            бре.токени = [дуплирај(т) for т in бре.токени]
        бре.директан_говор = False

    def __call__(бре):
        бре.и = iter(бре.токени)
        т = next(бре.и, КРАЈ)
        while not крај(т):
            т = бре.линија(т)
        return [л.strip() for л in бре.линије]

    def додај(бре, линија):
        if линија == '' and (бре.линије and бре.линије[-1] == ''):
            return
        if линија == '' and бре.директан_говор:
            return
        if бре.директан_говор:
            бре.линије.append(бре.наводник + линија + бре.наводник)
        else:
            бре.линије.append(линија)

    def линија(бре, т):
        if крај(т):
            return т
        л = ""
        if спејс(т):
            т = next(бре.и, КРАЈ)
            if крај(т):
                бре.додај(л)
                return т
        while True:
            if т.текст == бре.наводник and not бре.директан_говор:
                if л != "":
                    бре.додај(л)
                т = next(бре.и, КРАЈ)
                бре.директан_говор = True
                return т
            elif т.текст == бре.наводник and бре.директан_говор:
                бре.додај(л)
                т = next(бре.и, КРАЈ)
                бре.директан_говор = False
                return т
            elif т.текст == '\n':
                бре.додај(л)
                бре.додај('')
                т = next(бре.и, КРАЈ)
                return т
            elif крај_реченице(т):
                л += т.текст
                бре.додај(л)
                п = т
                т = next(бре.и, КРАЈ)
                if бре.директан_говор and п.текст == '.' and т.текст == бре.наводник:
                    бре.линије.append('')
                else:
                    бре.додај('')
                return т
            elif крај_дела_реченице(т):
                л += т.текст
                бре.додај(л)
                т = next(бре.и, КРАЈ)
                return т
            elif крај(т):
                бре.додај(л)
                return т
            else:
                л += т.текст
                т = next(бре.и, КРАЈ)

    # def директан_говор(бре, т):
    #     л = ""
    #     п = КРАЈ
    #     while True:
    #         if т.текст == бре.наводник:
    #             л += т.текст
    #             т = next(бре.и, КРАЈ)
    #             return т, л, п
    #         elif крај(т):
    #             return т, л, п
    #         else:
    #             л += т.текст
    #             п = т
    #             т = next(бре.и, КРАЈ)

