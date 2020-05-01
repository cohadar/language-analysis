from grimm.токенизер import Токенизер
from grimm.цитатор import Цитатор


def обрада(текст):
    ток = Токенизер(текст)
    токени = ток()
    цит = Цитатор(токени)
    токени = цит()
    return ''.join([т.текст for т in токени])


def test_цитат1():
    текст = 'trla "baba," lan'
    линије = обрада(текст)
    assert линије == 'trla „baba,“ lan'


# def test_цитат2():
#     текст = '"Dobar dan: Kako ste?"'
#     ток = Токенизер(текст)
#     токени = ток()
#     assert '„Dobar dan: Kako ste?“' == ''.join([т.текст for т in токени])


# def test_цитат3():
#     текст = '"Das sollst du alles haben" sprach das Männchen'
#     ток = Токенизер(текст)
#     токени = ток()
#     такст = '„Das sollst du alles haben“ sprach das Männchen'
#     assert такст == ''.join([т.текст for т in токени])


# def test_цитат4():
#     текст = '"daß es eine Art hat;" nahm'
#     ток = Токенизер(текст)
#     токени = ток()
#     такст = '„daß es eine Art hat;“ nahm'
#     assert такст == ''.join([т.текст for т in токени])


# def test_цитат5():
#     текст = 'und sagte:"Wenn ich auch wollte."'
#     ток = Токенизер(текст)
#     токени = ток()
#     такст = 'und sagte:„Wenn ich auch wollte.“'
#     assert такст == ''.join([т.текст for т in токени])


# def test_цитат6():
#     текст = '"hier Rebhühner"; wußte der'
#     ток = Токенизер(текст)
#     токени = ток()
#     такст = '„hier Rebhühner“; wußte der'
#     assert такст == ''.join([т.текст for т in токени])


# def test_цитат7():
#     текст = '"nicht gewettet, " sprach der Junge'
#     ток = Токенизер(текст)
#     токени = ток()
#     такст = '„nicht gewettet, “ sprach der Junge'
