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


def test_реченица():
    текст = 'trläÄ'
    assert ли(текст) == [текст]


def test_једна_линија():
    текст = 'trläÄ böÖba lanßüÜ meh'
    assert ли(текст) == [текст]


def test_исте_линије():
    текст = 'trläÄ\nböÖba lanßüÜ\nmeh'
    assert ли(текст) == ['trläÄ\n', 'böÖba lanßüÜ\n', 'meh']


def test_линија_крај():
    текст = 'trläÄ\n'
    assert ли(текст) == [текст]


def test_линија_почетак():
    текст = '\ntrläÄ'
    assert ли(текст) == ['\n', 'trläÄ']


def test_крајеви_реченица():
    текст = 'Dobar dan.Kako ste?Ja super!Hvala'
    assert ли(текст) == ['Dobar dan.\n\n', 'Kako ste?\n\n', 'Ja super!\n\n', 'Hvala']


def test_уклањање_почетног_спејса():
    текст = 'Dobar dan. Kako ste? Ja super! Hvala'
    assert ли(текст) == ['Dobar dan.\n\n', 'Kako ste?\n\n', 'Ja super!\n\n', 'Hvala']


def test_ломљење_зареза():
    текст = 'Dobar dan; Kako ste, Ja super, Hvala'
    assert ли(текст) == ['Dobar dan;\n', 'Kako ste,\n', 'Ja super,\n', 'Hvala']


def test_ломљење_двотачке():
    текст = 'Dobar dan: Kako ste'
    assert ли(текст) == ['Dobar dan:\n', 'Kako ste']


def test_почетни_цитат_не_ломи():
    текст = '"Dobar dan!"'
    assert ли(текст) == ['„Dobar dan!“']


def test_директан_говор_ломљење_двотачке():
    текст = '"Dobar dan: Kako ste?"'
    assert ли(текст) == ['„Dobar dan:“\n', '„Kako ste?“']


def test_директан_говор():
    текст = 'der sprach: "Bruder Hund. warum bist du! so traurig?"'
    assert ли(текст) == ['der sprach:\n', '„Bruder Hund.“\n', '„warum bist du!“\n', '„so traurig?“']


def test_директан_говор_ломи_линију_након():
    текст = 'zum Hunde: "Da bleib stehen, ich will dir unterpicken," setzte sich auf den Laden'
    assert ли(текст) == ['zum Hunde:\n', '„Da bleib stehen,“\n', '„ich will dir unterpicken,“\n', 'setzte sich auf den Laden']


def test_директан_говор_ломи_линију_са_узвиком():
    текст = '"Ach, ich armer Mann!" rief er.'
    assert ли(текст) == ['„Ach, ich armer Mann!“\n', 'rief er.']


def test_директан_говор_ломи_линију_са_питањем():
    текст = '"Bruder Hund, warum bist du so traurig?" Antwortete der Hund: "Ich bin hungrig."'
    assert ли(текст) == ['„Bruder Hund,“\n', '„warum bist du so traurig?“\n', 'Antwortete der Hund:\n', '„Ich bin hungrig.“']


def test_директан_говор_ломи_линију_са_тачком():
    текст = '"Bruder Hund, warum bist du so traurig." Antwortete der Hund: "Ich bin hungrig."'
    assert ли(текст) == ['„Bruder Hund,“\n', '„warum bist du so traurig.“\n', 'Antwortete der Hund:\n', '„Ich bin hungrig.“']


def test_директан_говор_тачка_ломи_јаче():
    текст = '"trla baba lan." da joj prodje dan'
    assert ли(текст) == ['„trla baba lan.“\n', 'da joj prodje dan']


def test_не_раздвајај_залепљену_интерпункцију():
    текст = 'trla baba lan.!? da joj prodje dan'
    assert ли(текст) == ['trla baba lan.!?\n\n', 'da joj prodje dan']


def test_крај_реченице_дупла_нова1():
    текст = 'trla baba lan. da joj prodje dan'
    assert ли(текст) == ['trla baba lan.\n\n', 'da joj prodje dan']


def test_крај_реченице_дупла_нова2():
    текст = 'trla baba lan! da joj prodje dan'
    assert ли(текст) == ['trla baba lan!\n\n', 'da joj prodje dan']


def test_крај_реченице_дупла_нова3():
    текст = 'trla baba lan? da joj prodje dan'
    assert ли(текст) == ['trla baba lan?\n\n', 'da joj prodje dan']


def test_крај_реченице_није_дупла_у_наводницима():
    текст = 'Er: "trla baba lan. da joj prodje dan."'
    assert ли(текст) == ['Er:\n', '„trla baba lan.“\n', '„da joj prodje dan.“']


def test_црта_између_наводника():
    текст = 'Da rief der Fuhrmann: „Ach, ich armer Mann!“ - „Noch nicht arm genug,“ antwortete der Sperling.'
    assert ли(текст) == [
        'Da rief der Fuhrmann:\n',
        '„Ach, ich armer Mann!“\n',
        '–\n',
        '„Noch nicht arm genug,“\n',
        'antwortete der Sperling.'
    ]


def test_не_ломи_зарез_у_цитату_после_једне_речи_на_почетку():
    текст = '"Fuhrmann, tu\'s nicht, oder ich mache dich arm!"'
    assert ли(текст) == [
        '„Fuhrmann, tu\'s nicht,“\n',
        '„oder ich mache dich arm!“'
    ]


