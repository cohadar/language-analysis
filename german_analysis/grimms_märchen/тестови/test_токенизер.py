from grimm.токенизер import Токенизер


def test_просте_речи():
    текст = 'trläÄ böÖba lanßüÜ'
    ток = Токенизер(текст)
    токени = ток()
    assert len(токени) == 6
    assert текст == ''.join([т.текст for т in токени])


def test_сепаратори():
    текст = 'trlä: böba, lanß.'
    ток = Токенизер(текст)
    токени = ток()
    assert len(токени) == 9
    assert текст == ''.join([т.текст for т in токени])
    assert токени[1].текст == ':'
    assert токени[4].текст == ','
    assert токени[-2].текст == '.'


def test_сепаратори_још():
    текст = 'tr-lä; ba=ba!'
    ток = Токенизер(текст)
    токени = ток()
    assert len(токени) == 10
    assert текст == ''.join([т.текст for т in токени])
    assert токени[1].текст == '-'
    assert токени[3].текст == ';'
    assert токени[6].текст == '='
    assert токени[-2].текст == '!'


def test_сепаратори_још2():
    текст = 'trlä\n[baba](lan)?'
    ток = Токенизер(текст)
    токени = ток()
    assert len(токени) == 10
    assert текст == ''.join([т.текст for т in токени])
    assert токени[1].текст == '\n'
    assert токени[2].текст == '['
    assert токени[4].текст == ']'
    assert токени[5].текст == '('
    assert токени[7].текст == ')'
    assert токени[-2].текст == '?'


def test_сепаратори_неаски():
    текст = 'trläba–ba ›lan‹'
    ток = Токенизер(текст)
    токени = ток()
    assert len(токени) == 8
    assert текст == ''.join([т.текст for т in токени])
    assert токени[1].текст == '–'
    assert токени[4].текст == '›'
    assert токени[6].текст == '‹'


def test_сепаратори_сумњиви():
    текст = 'trläba^ba/ba'
    ток = Токенизер(текст)
    токени = ток()
    assert len(токени) == 6
    assert текст == ''.join([т.текст for т in токени])
    assert токени[1].текст == '^'
    assert токени[3].текст == '/'


def test_број():
    текст = 'trläba123 baba'
    ток = Токенизер(текст)
    токени = ток()
    assert len(токени) == 5
    assert текст == ''.join([т.текст for т in токени])
    assert токени[1].текст == '123'


def test_цитат1():
    текст = 'trla "baba," lan'
    ток = Токенизер(текст)
    токени = ток()
    assert len(токени) == 9
    assert 'trla „baba,“ lan' == ''.join([т.текст for т in токени])
    assert токени[2].текст == '„'
    assert токени[5].текст == '“'


def test_цитат2():
    текст = '"Dobar dan: Kako ste?"'
    ток = Токенизер(текст)
    токени = ток()
    assert '„Dobar dan: Kako ste?“' == ''.join([т.текст for т in токени])


def test_цитат3():
    текст = '"Das sollst du alles haben" sprach das Männchen'
    ток = Токенизер(текст)
    токени = ток()
    такст = '„Das sollst du alles haben“ sprach das Männchen'
    assert такст == ''.join([т.текст for т in токени])


def test_цитат4():
    текст = '"daß es eine Art hat;" nahm'
    ток = Токенизер(текст)
    токени = ток()
    такст = '„daß es eine Art hat;“ nahm'
    assert такст == ''.join([т.текст for т in токени])


def test_цитат5():
    текст = 'und sagte:"Wenn ich auch wollte."'
    ток = Токенизер(текст)
    токени = ток()
    такст = 'und sagte:„Wenn ich auch wollte.“'
    assert такст == ''.join([т.текст for т in токени])


def test_цитат6():
    текст = '"hier Rebhühner"; wußte der'
    ток = Токенизер(текст)
    токени = ток()
    такст = '„hier Rebhühner“; wußte der'
    assert такст == ''.join([т.текст for т in токени])

