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
    текст = 'sagte: "Damit"'
    assert ц(текст) == 'sagte: „Damit“'


