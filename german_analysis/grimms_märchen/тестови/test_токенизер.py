from grimm.токенизер import Токенизер


def test_просте_речи():
    текст = 'trläÄ böÖba lanßüÜ'
    ток = Токенизер(текст)
    ток()
    assert len(ток.токени) == 6
    assert текст == ''.join([т.текст for т in ток.токени])


def test_сепаратори():
    текст = 'trlä: böba, "lanß.'
    ток = Токенизер(текст)
    ток()
    assert len(ток.токени) == 10
    assert текст == ''.join([т.текст for т in ток.токени])
    assert ток.токени[1].текст == ':'
    assert ток.токени[4].текст == ','
    assert ток.токени[6].текст == '"'
    assert ток.токени[-2].текст == '.'


def test_сепаратори_још():
    текст = 'tr-lä; \'ba=ba!'
    ток = Токенизер(текст)
    ток()
    assert len(ток.токени) == 11
    assert текст == ''.join([т.текст for т in ток.токени])
    assert ток.токени[1].текст == '-'
    assert ток.токени[3].текст == ';'
    assert ток.токени[5].текст == '\''
    assert ток.токени[7].текст == '='
    assert ток.токени[-2].текст == '!'


def test_сепаратори_још2():
    текст = 'trlä\n[baba](lan)?'
    ток = Токенизер(текст)
    ток()
    assert len(ток.токени) == 10
    assert текст == ''.join([т.текст for т in ток.токени])
    assert ток.токени[1].текст == '\n'
    assert ток.токени[2].текст == '['
    assert ток.токени[4].текст == ']'
    assert ток.токени[5].текст == '('
    assert ток.токени[7].текст == ')'
    assert ток.токени[-2].текст == '?'


def test_сепаратори_неаски():
    текст = 'trläba–ba ›lan‹'
    ток = Токенизер(текст)
    ток()
    assert len(ток.токени) == 8
    assert текст == ''.join([т.текст for т in ток.токени])
    assert ток.токени[1].текст == '–'
    assert ток.токени[4].текст == '›'
    assert ток.токени[6].текст == '‹'


def test_број():
    текст = 'trläba123 baba'
    ток = Токенизер(текст)
    ток()
    assert len(ток.токени) == 5
    assert текст == ''.join([т.текст for т in ток.токени])
    assert ток.токени[1].текст == '123'

