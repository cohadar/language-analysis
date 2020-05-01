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
    текст = '"Dobar dan: Kako ste?"'
    линије = тл(текст)
    assert линије == ['"Dobar dan:"', '"Kako ste?"']


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


def test_директан_говор_тачка_ломи_јаче():
    текст = '"trla baba lan." da joj prodje dan'
    линије = тл(текст)
    assert линије == ['"trla baba lan."', '', 'da joj prodje dan']


def test_цитат1():
    текст = 'trla "baba," lan'
    линије = тл(текст)
    assert линије == ['trla', '„baba,“', 'lan']


# def test_цитат2():
#     текст = '"Dobar dan: Kako ste?"'
#     ток = Токенизер(текст)
#     токени = ток()
#     assert '„Dobar dan: Kako ste?“' == ''.join([т.текст for т in токени])


# def test_цитат3():
#     текст = '"Das sollst du alles haben" sprach das Männchen'
#     ток = Токенизер(текст)
#     токени = ток()
#     такст = '„Das sollst du alles haben“ sprach das Männchen'
#     assert такст == ''.join([т.текст for т in токени])


# def test_цитат4():
#     текст = '"daß es eine Art hat;" nahm'
#     ток = Токенизер(текст)
#     токени = ток()
#     такст = '„daß es eine Art hat;“ nahm'
#     assert такст == ''.join([т.текст for т in токени])


# def test_цитат5():
#     текст = 'und sagte:"Wenn ich auch wollte."'
#     ток = Токенизер(текст)
#     токени = ток()
#     такст = 'und sagte:„Wenn ich auch wollte.“'
#     assert такст == ''.join([т.текст for т in токени])


# def test_цитат6():
#     текст = '"hier Rebhühner"; wußte der'
#     ток = Токенизер(текст)
#     токени = ток()
#     такст = '„hier Rebhühner“; wußte der'
#     assert такст == ''.join([т.текст for т in токени])


# def test_цитат7():
#     текст = '"nicht gewettet, " sprach der Junge'
#     ток = Токенизер(текст)
#     токени = ток()
#     такст = '„nicht gewettet, “ sprach der Junge'
