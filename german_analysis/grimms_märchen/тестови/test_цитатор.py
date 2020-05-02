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


def test_цитат0():
    текст = 'sagte: „Damit“'
    assert ц(текст) == текст


def test_цитат1():
    текст = 'sagte: "Damit"'
    assert ц(текст) == 'sagte: „Damit“'


def test_цитат2():
    текст = ': "der Hund"'
    assert ц(текст) == ': „der Hund“'


def test_цитат3():
    текст = '"spazieren gehen." Da'
    assert ц(текст) == '„spazieren gehen.“ Da'


def test_цитат4():
    текст = '"spazieren gehen," Da'
    assert ц(текст) == '„spazieren gehen,“ Da'


def test_цитат5():
    текст = 'sagte:\n"Hallo, Mark"'
    assert ц(текст) == 'sagte:\n„Hallo, Mark“'

