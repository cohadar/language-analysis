from grimm.токенизер import Токенизер


def test_просте_речи():
    текст = 'trla baba lan'
    ток = Токенизер(текст)
    ток()
    assert len(ток.токени) == 6
    assert текст == ''.join([т.текст for т in ток.токени])

