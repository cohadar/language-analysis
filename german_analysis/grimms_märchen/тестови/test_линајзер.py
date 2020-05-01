from grimm.токенизер import Токенизер
from grimm.линајзер import Линајзер
from grimm.цитатор import Цитатор


def л(текст):
    ток = Токенизер(текст)
    токени = ток()
    цит = Цитатор(токени)
    токени = цит()
    лин = Линајзер(токени)
    лин()
    return str(лин)


def test_реч():
    текст = 'trläÄ'
    assert л(текст) == текст


def test_једна_линија():
    текст = 'trläÄ böÖba lanßüÜ meh'
    assert л(текст) == текст


def test_исте_линије():
    текст = 'trläÄ\nböÖba lanßüÜ\nmeh'
    assert л(текст) == текст


def test_линија_крај():
    текст = 'trläÄ\n'
    assert л(текст) == текст


def test_линија_почетак():
    текст = '\ntrläÄ'
    assert л(текст) == текст


def test_крајеви_реченица():
    текст = 'Dobar dan.Kako ste?Ja super!Hvala'
    assert л(текст) == 'Dobar dan.\nKako ste?\nJa super!\nHvala'


def test_уклањање_почетног_спејса():
    текст = 'Dobar dan. Kako ste? Ja super! Hvala'
    assert л(текст) == 'Dobar dan.\nKako ste?\nJa super!\nHvala'


# def test_ломљење_зареза():
#     текст = 'Dobar dan; Kako ste, Ja super, Hvala'
#     assert л(текст) == 'Dobar dan;\nKako ste,\nJa super,\nHvala'


# def test_ломљење_двотачке():
#     текст = 'Dobar dan: Kako ste'
#     assert л(текст) == 'Dobar dan:\nKako ste'


# def test_почетни_цитат_не_ломи():
#     текст = '"Dobar dan!"'
#     assert л(текст) == '„Dobar dan!“'


# def test_директан_говор_ломљење_двотачке():
#     текст = '"Dobar dan: Kako ste?"'
#     assert л(текст) == '„Dobar dan:“\n„Kako ste?“'


# def test_директан_говор():
#     текст = 'der sprach: "Bruder Hund. warum bist du! so traurig?"'
#     assert л(текст) == 'der sprach:\n„Bruder Hund.“\n„warum bist du!“\n„so traurig?“'


# def test_директан_говор_ломи_линију_након():
#     текст = 'zum Hunde: "Da bleib stehen, ich will dir unterpicken," setzte sich auf den Laden'
#     assert л(текст) == 'zum Hunde:\n„Da bleib stehen,“\n„ich will dir unterpicken,“\nsetzte sich auf den Laden'


# def test_директан_говор_ломи_линију_са_узвиком():
#     текст = '"Ach, ich armer Mann!" rief er.'
#     assert л(текст) == '„Ach,“\n„ich armer Mann!“\nrief er.'


# def test_директан_говор_ломи_линију_са_питањем():
#     текст = '"Bruder Hund, warum bist du so traurig?" Antwortete der Hund: "Ich bin hungrig."'
#     assert л(текст) == '„Bruder Hund,“\n„warum bist du so traurig?“\nAntwortete der Hund:\n„Ich bin hungrig.“'


# def test_директан_говор_ломи_линију_са_тачком():
#     текст = '"Bruder Hund, warum bist du so traurig." Antwortete der Hund: "Ich bin hungrig."'
#     assert л(текст) == '„Bruder Hund,“\n„warum bist du so traurig.“\nAntwortete der Hund:\n„Ich bin hungrig.“'


# def test_директан_говор_тачка_ломи_јаче():
#     текст = '"trla baba lan." da joj prodje dan'
#     assert л(текст) == '„trla baba lan.“\nda joj prodje dan'

