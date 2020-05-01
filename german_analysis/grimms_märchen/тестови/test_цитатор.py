import pytest
from grimm.токенизер import Токенизер
from grimm.цитатор import Цитатор, ЦитатГрешка


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


def test_цитат7():
    текст = '"das, " das'
    with pytest.raises(ЦитатГрешка):
        ц(текст)


def test_цитат8():
    текст = '"sprach: " Nun'
    with pytest.raises(ЦитатГрешка):
        ц(текст)


def test_цитат9():
    текст = '"Welt. " Er'
    with pytest.raises(ЦитатГрешка):
        ц(текст)


def test_цитат10():
    текст = '"heraus!" -"Nein,"'
    assert ц(текст) == '„heraus!“ -„Nein,“'


def test_цитат11():
    текст = '"sagst: ›Knüppel, in den Sack!‹" Der'
    assert ц(текст) == '„sagst: ›Knüppel, in den Sack!‹“ Der'


def test_цитат12():
    текст = '"tät\' ihr zerspringen!\'"'
    assert ц(текст) == '„tät\' ihr zerspringen!\'“'


def test_цитат13():
    текст = 'Kopf ."Was ist"'
    with pytest.raises(ЦитатГрешка):
        ц(текст)


def test_цитат14():
    текст = 'sagte:" Ich"'
    assert ц(текст) == 'sagte:„ Ich“'


def test_цитат15():
    текст = '"Welt."Er'
    with pytest.raises(ЦитатГрешка):
        ц(текст)


def test_цитат16():
    текст = '"Welt." Er'
    assert ц(текст) == '„Welt.“ Er'

