from grimm.токенизер import Токенизер
from grimm.токенизер import ТОКЕН_ОТВОРЕНИ_НАВОДНИК, ТОКЕН_ЗАТВОРЕНИ_НАВОДНИК


def тт(текст):
    ток = Токенизер(текст)
    токени = ток()
    return [т.текст for т in токени]


def test_просте_речи():
    текст = 'trläÄ böÖba lanßüÜ'
    assert тт(текст) == ['trläÄ', ' ', 'böÖba', ' ', 'lanßüÜ', '']


def test_сепаратори():
    текст = 'trlä: böba, lanß.'
    assert тт(текст) == ['trlä', ':', ' ', 'böba', ',', ' ', 'lanß', '.', '']


def test_сепаратори_још():
    текст = 'tr-lä; ba=ba!'
    assert тт(текст) == ['tr', '-', 'lä', ';', ' ', 'ba', '=', 'ba', '!', '']


def test_сепаратори_још2():
    текст = 'trlä\n[baba](lan)?'
    assert тт(текст) == ['trlä', '\n', '[', 'baba', ']', '(', 'lan', ')', '?', '']


def test_сепаратори_неаски():
    текст = 'trläba–ba ›lan‹'
    assert тт(текст) == ['trläba', '–', 'ba', ' ', '›', 'lan', '‹', '']


def test_сепаратори_сумњиви():
    текст = 'trläba^ba/ba'
    assert тт(текст) == ['trläba', '^', 'ba', '/', 'ba', '']


def test_број():
    текст = 'trläba123 baba'
    assert тт(текст) == ['trläba', '123', ' ', 'baba', '']


def test_наводници1():
    текст = '„la“'
    assert тт(текст) == ['„', 'la', '“', '']


def test_додато_ес():
    текст = "Wenn's Ist's\nEr's"
    assert тт(текст) == ["Wenn's", ' ', "Ist's", '\n', "Er's", '']


