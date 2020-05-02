from grimm.токенизер import ТОКЕН_ЗА_ПОЧЕТАК, ТОКЕН_ЗА_КРАЈ
from grimm.токенизер import ТОКЕН_ЊАК
from grimm.токенизер import ТОКЕН_ОТВОРЕНИ_НАВОДНИК, ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК
from grimm.токенизер import је_реч, је_спејс, је_неодређени_наводник, је_токен_за_крај
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
        if је_неодређени_наводник(т):
            бре.излаз.append(бре.наводник())
        else:
            бре.излаз.append(т)

    def __str__(бре):
        return ''.join((т.текст for т in бре.излаз))

    def цитат_грешка(бре):
        досад = ''.join([т.текст for т in бре.излаз])
        raise ЦитатГрешка(f'Лош цитат: ({бре.и.тренутно}), линија={бре.и.линија}, текст={досад[-100:]}')

    def одреди_наводник(бре, пре2, прет, след):
        if пре2.текст == ':' and је_спејс(прет) and је_реч(след):
            return ТОКЕН_ОТВОРЕНИ_НАВОДНИК
        if је_реч(прет) and је_токен_за_крај(след):
            return ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК
        return None

    def наводник(бре):
        н = бре.одреди_наводник(бре.и.пре_два, бре.и.претходно, бре.и.следеће)
        if н:
            return н
        бре.цитат_грешка()

