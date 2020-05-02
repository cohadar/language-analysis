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
    текст = 'sagte: „Damit“ ist'
    assert ц(текст) == текст


def test_на_крају_текста1():
    текст = 'sagte: "Damit"'
    assert ц(текст) == 'sagte: „Damit“'


def test_на_крају_текста2():
    текст = '"der Hund"'
    assert ц(текст) == '„der Hund“'


def test_на_крају_текста3():
    текст = '"zwiter lied."'
    assert ц(текст) == '„zwiter lied.“'


def test_затворен_цитат1():
    текст = '"spazieren gehen." Da'
    assert ц(текст) == '„spazieren gehen.“ Da'


def test_затворен_цитат2():
    текст = '"spazieren gehen," Da'
    assert ц(текст) == '„spazieren gehen,“ Da'


def test_затворен_цитат3():
    текст = '"erste lied."\n"zwiter lied."'
    assert ц(текст) == '„erste lied.“\n„zwiter lied.“'


def test_затворен_цитат4():
    текст = '"Wer war das?" - ich.'
    assert ц(текст) == '„Wer war das?“ - ich.'


def test_затворен_цитат5():
    текст = '"Das soll dir schlecht bekommen." - Meh'
    assert ц(текст) == '„Das soll dir schlecht bekommen.“ - Meh'


def test_на_почетку_текста():
    текст = '"Hallo Leute"'
    assert ц(текст) == '„Hallo Leute“'


def test_цитат5():
    текст = 'sagte:\n"Hallo, Mark"'
    assert ц(текст) == 'sagte:\n„Hallo, Mark“'




def test_цитат8():
    текст = 'sagte der Hirt, "Hello Mark"'
    assert ц(текст) == 'sagte der Hirt, „Hello Mark“'




def test_цитат10():
    текст = 'Mann - "Ach," antwortete sie'
    assert ц(текст) == 'Mann - „Ach,“ antwortete sie'


def test_цитат11():
    текст = 'sich stehen. "Wie kannst"'
    assert ц(текст) == 'sich stehen. „Wie kannst“'


