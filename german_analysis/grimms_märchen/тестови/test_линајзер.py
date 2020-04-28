from grimm.токенизер import Токенизер
from grimm.линајзер import Линајзер


def тл(текст):
    ток = Токенизер(текст)
    токени = ток()
    лин = Линајзер(токени)
    return лин()


def test_нове_линије():
    текст = 'trläÄ\nböÖba lanßüÜ\nmeh'
    линије = тл(текст)
    assert len(линије) == 3
    assert текст == '\n'.join(линије)


def test_крајеви_реченица():
    текст = 'Dobar dan. Kako ste? Ja super! Hvala'
    линије = тл(текст)
    assert len(линије) == 4
    assert линије[0] == 'Dobar dan.'
    assert линије[1] == ' Kako ste?'
    assert линије[2] == ' Ja super!'
    assert линије[3] == ' Hvala'


def test_директан_говор():
    текст = 'der sprach: "Bruder Hund. warum bist! du so traurig?"'
    линије = тл(текст)
    assert len(линије) == 1
    assert линије[0] == текст

