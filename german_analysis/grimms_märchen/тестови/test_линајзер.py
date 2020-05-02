from grimm.токенизер import Токенизер
from grimm.линајзер import Линајзер
from grimm.цитатор import Цитатор


def ли(текст):
    ток = Токенизер(текст)
    токени = ток()
    цит = Цитатор(токени)
    токени = цит()
    лин = Линајзер(токени)
    лин()
    return лин.линије


def test_реч():
    текст = 'trläÄ'
    assert ли(текст) == [текст]


def test_једна_линија():
    текст = 'trläÄ böÖba lanßüÜ meh'
    assert ли(текст) == [текст]


def test_исте_линије():
    текст = 'trläÄ\nböÖba lanßüÜ\nmeh'
    assert ли(текст) == ['trläÄ\n', 'böÖba lanßüÜ\n', 'meh']


# def test_линија_крај():
#     текст = 'trläÄ\n'
#     assert ли(текст) == [текст]


# def test_линија_почетак():
#     текст = '\ntrläÄ'
#     assert ли(текст) == ['\n', 'trläÄ']


# def test_крајеви_реченица():
#     текст = 'Dobar dan.Kako ste?Ja super!Hvala'
#     assert ли(текст) == ['Dobar dan.\n', 'Kako ste?\n', 'Ja super!\n', 'Hvala']


# def test_уклањање_почетног_спејса():
#     текст = 'Dobar dan. Kako ste? Ja super! Hvala'
#     assert ли(текст) == ['Dobar dan.\n', 'Kako ste?\n', 'Ja super!\n', 'Hvala']


# def test_ломљење_зареза():
#     текст = 'Dobar dan; Kako ste, Ja super, Hvala'
#     assert ли(текст) == ['Dobar dan;\n', 'Kako ste,\n', 'Ja super,\n', 'Hvala']


# def test_ломљење_двотачке():
#     текст = 'Dobar dan: Kako ste'
#     assert ли(текст) == ['Dobar dan:\n', 'Kako ste']


# def test_почетни_цитат_не_ломи():
#     текст = '"Dobar dan!"'
#     assert ли(текст) == ['„Dobar dan!“']


# def test_директан_говор_ломљење_двотачке():
#     текст = '"Dobar dan: Kako ste?"'
#     assert ли(текст) == ['„Dobar dan:“\n', '„Kako ste?“']


# def test_директан_говор():
#     текст = 'der sprach: "Bruder Hund. warum bist du! so traurig?"'
#     assert ли(текст) == ['der sprach:\n', '„Bruder Hund.“\n', '„warum bist du!“\n', '„so traurig?“']


# def test_директан_говор_ломи_линију_након():
#     текст = 'zum Hunde: "Da bleib stehen, ich will dir unterpicken," setzte sich auf den Laden'
#     assert ли(текст) == ['zum Hunde:\n', '„Da bleib stehen,“\n', '„ich will dir unterpicken,“\n', 'setzte sich auf den Laden']


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

