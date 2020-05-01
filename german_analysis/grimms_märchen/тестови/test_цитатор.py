from grimm.токенизер import Токенизер
from grimm.цитатор import Цитатор


def ц(текст):
    ток = Токенизер(текст)
    токени = ток()
    for т in токени:
        assert len(т.текст) >= 0, т
    цит = Цитатор(токени)
    токени = цит()
    return str(цит)


def test_цитат1():
    текст = 'trla "baba," lan'
    assert ц(текст) == 'trla „baba,“ lan'


def test_цитат2():
    текст = '"Dobar dan: Kako ste?"'
    assert ц(текст) == '„Dobar dan: Kako ste?“'


def test_цитат3():
    текст = '"Das sollst du alles haben" sprach das Männchen'
    assert ц(текст) == '„Das sollst du alles haben“ sprach das Männchen'


def test_цитат4():
    текст = '"daß es eine Art hat;" nahm'
    assert ц(текст) == '„daß es eine Art hat;“ nahm'


def test_цитат5():
    текст = 'und sagte:"Wenn ich auch wollte."'
    assert ц(текст) == 'und sagte:„Wenn ich auch wollte.“'


def test_цитат6():
    текст = '"hier Rebhühner"; wußte der'
    assert ц(текст) == '„hier Rebhühner“; wußte der'


# def test_цитат7():
#     текст = '"nicht gewettet, " sprach der Junge'
#     assert ц(текст) == '„nicht gewettet, “ sprach der Junge'

