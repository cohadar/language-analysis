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
    текст = 'Dobar dan.Kako ste?Ja super!Hvala'
    линије = тл(текст)
    assert len(линије) == 4
    assert линије[0] == 'Dobar dan.'
    assert линије[1] == 'Kako ste?'
    assert линије[2] == 'Ja super!'
    assert линије[3] == 'Hvala'


def test_уклањање_почетног_спејса():
    текст = 'Dobar dan. Kako ste? Ja super! Hvala'
    линије = тл(текст)
    assert len(линије) == 4
    assert линије[0] == 'Dobar dan.'
    assert линије[1] == 'Kako ste?'
    assert линије[2] == 'Ja super!'
    assert линије[3] == 'Hvala'


def test_директан_говор():
    текст = 'der sprach: "Bruder Hund. warum bist! du so traurig?"'
    линије = тл(текст)
    assert len(линије) == 1
    assert линије[0] == текст

    текст = "der sprach: 'Bruder Hund. warum bist! du so traurig?'"
    линије = тл(текст)
    assert len(линије) == 1
    assert линије[0] == текст


def test_директан_говор_не_ломи_линију():
    текст = 'zum Hunde: "Da bleib stehen, ich will dir unterpicken," setzte sich auf den Laden'
    линије = тл(текст)
    assert len(линије) == 1
    assert линије[0] == текст

    текст = "zum Hunde: 'Da bleib stehen, ich will dir unterpicken,' setzte sich auf den Laden"
    линије = тл(текст)
    assert len(линије) == 1
    assert линије[0] == текст


def test_директан_говор_ломи_линију_са_узвиком():
    текст = '"Ach, ich armer Mann!" rief er.'
    линије = тл(текст)
    assert len(линије) == 2
    assert линије[0] == '"Ach, ich armer Mann!"'
    assert линије[1] == 'rief er.'

    текст = "'Ach, ich armer Mann!' rief er."
    линије = тл(текст)
    assert len(линије) == 2
    assert линије[0] == "'Ach, ich armer Mann!'"
    assert линије[1] == "rief er."


def test_директан_говор_ломи_линију_са_питањем():
    текст = 'der sprach: "Bruder Hund, warum bist du so traurig?" Antwortete der Hund: "Ich bin hungrig."'
    линије = тл(текст)
    assert len(линије) == 2
    assert линије[0] == 'der sprach: "Bruder Hund, warum bist du so traurig?"'
    assert линије[1] == 'Antwortete der Hund: "Ich bin hungrig."'

    текст = "der sprach: 'Bruder Hund, warum bist du so traurig?' Antwortete der Hund: 'Ich bin hungrig.'"
    линије = тл(текст)
    assert len(линије) == 2
    assert линије[0] == "der sprach: 'Bruder Hund, warum bist du so traurig?'"
    assert линије[1] == "Antwortete der Hund: 'Ich bin hungrig.'"


def test_директан_говор_ломи_линију_са_тачком():
    текст = 'der sprach: "Bruder Hund, warum bist du so traurig." Antwortete der Hund: "Ich bin hungrig."'
    линије = тл(текст)
    assert len(линије) == 2
    assert линије[0] == 'der sprach: "Bruder Hund, warum bist du so traurig."'
    assert линије[1] == 'Antwortete der Hund: "Ich bin hungrig."'

    текст = "der sprach: 'Bruder Hund, warum bist du so traurig.' Antwortete der Hund: 'Ich bin hungrig.'"
    линије = тл(текст)
    assert len(линије) == 2
    assert линије[0] == "der sprach: 'Bruder Hund, warum bist du so traurig.'"
    assert линије[1] == "Antwortete der Hund: 'Ich bin hungrig.'"

