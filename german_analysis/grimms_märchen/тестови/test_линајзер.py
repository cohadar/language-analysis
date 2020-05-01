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


def test_ломљење_зареза():
    текст = 'Dobar dan; Kako ste, Ja super, Hvala'
    линије = тл(текст)
    assert len(линије) == 4
    assert линије[0] == 'Dobar dan;'
    assert линије[1] == 'Kako ste,'
    assert линије[2] == 'Ja super,'
    assert линије[3] == 'Hvala'


def test_ломљење_двотачке():
    текст = 'Dobar dan: Kako ste'
    линије = тл(текст)
    assert линије == ['Dobar dan:', 'Kako ste']


def test_директан_говор_ломљење_двотачке():
    текст = '"Dobar dan: Kako ste"'
    линије = тл(текст)
    assert линије == ['"Dobar dan:"', '"Kako ste"']


def test_директан_говор():
    текст = 'der sprach: "Bruder Hund. warum bist du! so traurig?"'
    линије = тл(текст)
    assert len(линије) == 4
    assert линије[0] == 'der sprach:'
    assert линије[1] == '"Bruder Hund."'
    assert линије[2] == '"warum bist du!"'
    assert линије[3] == '"so traurig?"'


def test_директан_говор_ломи_линију_након():
    текст = 'zum Hunde: "Da bleib stehen, ich will dir unterpicken," setzte sich auf den Laden'
    линије = тл(текст)
    assert len(линије) == 4
    assert линије[0] == 'zum Hunde:'
    assert линије[1] == '"Da bleib stehen,"'
    assert линије[2] == '"ich will dir unterpicken,"'
    assert линије[3] == 'setzte sich auf den Laden'


def test_директан_говор_ломи_линију_са_узвиком():
    текст = '"Ach, ich armer Mann!" rief er.'
    линије = тл(текст)
    assert len(линије) == 4
    assert линије[0] == '"Ach,"'
    assert линије[1] == '"ich armer Mann!"'
    assert линије[2] == 'rief er.'
    assert линије[3] == ''


def test_директан_говор_ломи_линију_са_питањем():
    текст = '"Bruder Hund, warum bist du so traurig?" Antwortete der Hund: "Ich bin hungrig."'
    линије = тл(текст)
    assert len(линије) == 5
    assert линије[0] == '"Bruder Hund,"'
    assert линије[1] == '"warum bist du so traurig?"'
    assert линије[2] == 'Antwortete der Hund:'
    assert линије[3] == '"Ich bin hungrig."'
    assert линије[4] == ''


def test_директан_говор_ломи_линију_са_тачком():
    текст = '"Bruder Hund, warum bist du so traurig." Antwortete der Hund: "Ich bin hungrig."'
    линије = тл(текст)
    assert len(линије) == 6
    assert линије[0] == '"Bruder Hund,"'
    assert линије[1] == '"warum bist du so traurig."'
    assert линије[2] == ''
    assert линије[3] == 'Antwortete der Hund:'
    assert линије[4] == '"Ich bin hungrig."'
    assert линије[5] == ''


def test_директан_говор_детектуј_наводнике():
    der = "d'r"
    текст = f'der sprach: "Bruder Hund, warum so traurig?" Antwortete {der} Hund: "Ich bin hungrig."'
    ток = Токенизер(текст)
    токени = ток()
    лин = Линајзер(токени)
    assert лин.наводник == '"'
    линије = лин()
    assert len(линије) == 6
    assert линије[0] == 'der sprach:'
    assert линије[1] == '"Bruder Hund,"'
    assert линије[2] == '"warum so traurig?"'
    assert линије[3] == f'Antwortete {der} Hund:'
    assert линије[4] == '"Ich bin hungrig."'
    assert линије[5] == ''


def test_директан_говор_тачка_ломи_јаче():
    текст = '"trla baba lan." da joj prodje dan'
    линије = тл(текст)
    assert линије == ['"trla baba lan."', '', 'da joj prodje dan']

