from pathlib import Path
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


def test_хммм():
    птњ = Path('/private/tmp/www.grimmstories.com/1/947e06105e02d6df25785c76f77d6ffe5b48a450359f664698964d3622fb8f23')
    with птњ.open('r') as ф:
        текст = ф.read()
        линије = тл(текст)
        assert len(линије) == 3
        assert текст == '\n'.join(линије)

