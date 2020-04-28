from grimm.токенизер import Токенизер
from grimm.линајзер import Линајзер


def тл(текст):
    ток = Токенизер(текст)
    токени = ток()
    лин = Линајзер(токени)
    return лин()


def test_просте_речи():
    текст = 'trläÄ\nböÖba lanßüÜ\nmeh'
    линије = тл(текст)
    assert len(линије) == 3
    assert текст == '\n'.join(линије)

