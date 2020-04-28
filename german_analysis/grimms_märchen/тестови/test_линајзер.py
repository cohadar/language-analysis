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
    assert len(линије) == 5
    assert линије[0] == 'trläÄ'
    assert линије[1] == ''
    assert линије[2] == 'böÖba lanßüÜ'
    assert линије[3] == ''
    assert линије[4] == 'meh'


def test_крајеви_реченица():
    текст = 'Dobar dan.Kako ste?Ja super!Hvala'
    линије = тл(текст)
    assert len(линије) == 7
    assert линије[0] == 'Dobar dan.'
    assert линије[1] == ''
    assert линије[2] == 'Kako ste?'
    assert линије[3] == ''
    assert линије[4] == 'Ja super!'
    assert линије[5] == ''
    assert линије[6] == 'Hvala'


def test_уклањање_почетног_спејса():
    текст = 'Dobar dan. Kako ste? Ja super! Hvala'
    линије = тл(текст)
    assert len(линије) == 7
    assert линије[0] == 'Dobar dan.'
    assert линије[1] == ''
    assert линије[2] == 'Kako ste?'
    assert линије[3] == ''
    assert линије[4] == 'Ja super!'
    assert линије[5] == ''
    assert линије[6] == 'Hvala'


def test_директан_говор():
    текст = 'der sprach: "Bruder Hund. warum bist du! so traurig?"'
    линије = тл(текст)
    assert len(линије) == 4
    assert линије[0] == 'der sprach:'
    assert линије[1] == '"Bruder Hund."'
    assert линије[2] == '"warum bist du!"'
    assert линије[3] == '"so traurig?"'


# def test_директан_говор_ломи_линију_након():
#     текст = 'zum Hunde: "Da bleib stehen, ich will dir unterpicken," setzte sich auf den Laden'
#     линије = тл(текст)
#     assert len(линије) == 3
#     assert линије[0] == 'zum Hunde:'
#     assert линије[1] == '"Da bleib stehen, ich will dir unterpicken,"'
#     assert линије[2] == 'setzte sich auf den Laden'


# def test_директан_говор_ломи_линију_са_узвиком():
#     текст = '"Ach, ich armer Mann!" rief er.'
#     линије = тл(текст)
#     assert len(линије) == 2
#     assert линије[0] == '"Ach, ich armer Mann!"'
#     assert линије[1] == 'rief er.'


# def test_директан_говор_ломи_линију_са_питањем():
#     текст = '"Bruder Hund, warum bist du so traurig?" Antwortete der Hund: "Ich bin hungrig."'
#     линије = тл(текст)
#     assert len(линије) == 3
#     assert линије[0] == '"Bruder Hund, warum bist du so traurig?"'
#     assert линије[1] == 'Antwortete der Hund:'
#     assert линије[2] == '"Ich bin hungrig."'


# def test_директан_говор_ломи_линију_са_тачком():
#     текст = '"Bruder Hund, warum bist du so traurig." Antwortete der Hund: "Ich bin hungrig."'
#     линије = тл(текст)
#     assert len(линије) == 3
#     assert линије[0] == '"Bruder Hund, warum bist du so traurig."'
#     assert линије[1] == 'Antwortete der Hund:'
#     assert линије[2] == '"Ich bin hungrig."'


# def test_директан_говор_се_не_прима_на_сваку_тачку():
#     текст = '"dobar dan. kako ste? ja super!" a vi?'
#     линије = тл(текст)
#     assert len(линије) == 2
#     assert линије[0] == '"dobar dan. kako ste? ja super!"'
#     assert линије[1] == 'a vi?'


# def test_директан_говор_детектуј_наводнике():
#     der = "d'r"
#     текст = f'der sprach: "Bruder Hund, warum so traurig." Antwortete {der} Hund: "Ich bin hungrig."'
#     ток = Токенизер(текст)
#     токени = ток()
#     лин = Линајзер(токени)
#     assert лин.наводник == '"'
#     линије = лин()
#     assert len(линије) == 4
#     assert линије[0] == 'der sprach:'
#     assert линије[1] == '"Bruder Hund, warum so traurig."'
#     assert линије[2] == f'Antwortete {der} Hund:'
#     assert линије[3] == f'"Ich bin hungrig."'


# def test_дуплирање_наводника():
#     текст = "'dobar dan. kako ste? ja super!' a vi?"
#     линије = тл(текст)
#     assert len(линије) == 2
#     assert линије[0] == '"dobar dan. kako ste? ja super!"'
#     assert линије[1] == 'a vi?'


# def test_дуплирање_наводника_неможе():
#     текст = "'dobar dan. kako ste? ja sup\"r!' a vi?"
#     линије = тл(текст)
#     assert len(линије) == 2
#     assert линије[0] == "'dobar dan. kako ste? ja sup\"r!'"
#     assert линије[1] == 'a vi?'


# def test_ломљење_зареза():
#     текст = "trla, baba lan, da joj prodje, dan."
#     линије = тл(текст)
#     assert len(линије) == 4
#     assert линије[0] == "trla,"
#     assert линије[1] == "baba lan,"
#     assert линије[2] == "da joj prodje,"
#     assert линије[3] == "dan."


# def test_ломљење_тачка_зареза():
#     текст = "trla, baba lan; da joj prodje, dan."
#     линије = тл(текст)
#     assert len(линије) == 4
#     assert линије[0] == "trla,"
#     assert линије[1] == "baba lan;"
#     assert линије[2] == "da joj prodje,"
#     assert линије[3] == "dan."

