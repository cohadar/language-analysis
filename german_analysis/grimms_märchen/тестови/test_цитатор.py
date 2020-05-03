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


def test_даш_трансформација():
    текст = ' - '
    assert ц(текст) == ' – '


def test_црта_на_крају_речи1():
    текст = 'vier- bis fünfhundertfältig'
    assert ц(текст) == 'vier- bis fünfhundertfältig'


def test_црта_на_крају_речи2():
    текст = 'hin- und hergehen'
    assert ц(текст) == 'hin- und hergehen'


def test_црта_на_крају_речи3():
    текст = 'fünfzig- oder sechzigfältig'
    assert ц(текст) == 'fünfzig- oder sechzigfältig'


def test_већ_цитирано():
    текст = 'sagte: „Damit“ ist'
    assert ц(текст) == текст


def test_на_крају_текста1():
    текст = '"Deine Mutter"'
    assert ц(текст) == '„Deine Mutter“'


def test_на_крају_текста2():
    текст = '"der Hund"'
    assert ц(текст) == '„der Hund“'


def test_на_крају_текста3():
    текст = '"zwiter lied."'
    assert ц(текст) == '„zwiter lied.“'


def test_затворен_цитат1():
    текст = '"spazieren gehen." Da'
    assert ц(текст) == '„spazieren gehen.“ Da'


def test_затворен_цитат2():
    текст = '"spazieren gehen," Da'
    assert ц(текст) == '„spazieren gehen,“ Da'


def test_затворен_цитат3():
    текст = '"erste lied."\n"zwiter lied."'
    assert ц(текст) == '„erste lied.“\n„zwiter lied.“'


def test_затворен_цитат4():
    текст = '"Wer war das?" - ich.'
    assert ц(текст) == '„Wer war das?“ – ich.'


def test_затворен_цитат5():
    текст = '"Das soll dir schlecht bekommen." - Meh'
    assert ц(текст) == '„Das soll dir schlecht bekommen.“ – Meh'


def test_затворен_цитат6():
    текст = '"Laß dein Haar herunter."\nso ließ sie die Haare hinab.'
    assert ц(текст) == '„Laß dein Haar herunter.“\nso ließ sie die Haare hinab.'


def test_затворен_цитат7():
    текст = '"doch betrogen!" In ihrem'
    assert ц(текст) == '„doch betrogen!“ In ihrem'


def test_затворен_цитат8():
    текст = '"Wie lauten die drei Fragen?" Der König sagte'
    assert ц(текст) == '„Wie lauten die drei Fragen?“ Der König sagte'


def test_затворен_цитат9():
    текст = '"Ewigkeit vorbei."\n\n'
    assert ц(текст) == '„Ewigkeit vorbei.“\n\n'


def test_затворен_сумњив1():
    текст = '"Das sollst du alles haben" sprach das Männchen'
    assert ц(текст) == '„Das sollst du alles haben“ sprach das Männchen'


def test_на_почетку_текста():
    текст = '"Hallo Leute"'
    assert ц(текст) == '„Hallo Leute“'


def test_након_двотачке1():
    текст = 'sagte: "Damit"'
    assert ц(текст) == 'sagte: „Damit“'


def test_након_двотачке2():
    текст = 'sagte: "Damit ich"'
    assert ц(текст) == 'sagte: „Damit ich“'


def test_након_двотачке3():
    текст = 'sprach zum Schneiderlein: "Mein, beiß"'
    assert ц(текст) == 'sprach zum Schneiderlein: „Mein, beiß“'


def test_након_двотачке4():
    текст = 'haben und sprach: " Nun, weißt du"'
    assert ц(текст) == 'haben und sprach: „ Nun, weißt du“'


def test_спојена_двотачка1():
    текст = 'nochmals und sagte:"Wenn ich"'
    assert ц(текст) == 'nochmals und sagte:„Wenn ich“'


def test_након_зареза1():
    текст = 'sagte der Hirt, "Hello Mark"'
    assert ц(текст) == 'sagte der Hirt, „Hello Mark“'


def test_након_зареза2():
    текст = 'der Junge, " die Bank ist mein."'
    assert ц(текст) == 'der Junge, „ die Bank ist mein.“'


def test_након_црте1():
    текст = 'Mann - "Ach," antwortete sie'
    assert ц(текст) == 'Mann – „Ach,“ antwortete sie'


def test_након_црте2():
    текст = '"Augenblick bei mir." - "Ach du"'
    assert ц(текст) == '„Augenblick bei mir.“ – „Ach du“'


def test_након_тачке1():
    текст = 'sich stehen. "Wie kannst"'
    assert ц(текст) == 'sich stehen. „Wie kannst“'


def test_након_тачке2():
    текст = 'Blicken ansah. "Aha," rief sie'
    assert ц(текст) == 'Blicken ansah. „Aha,“ rief sie'


def test_након_тачке3():
    текст = 'und fiel vor ihn hin. "Heda!"'
    assert ц(текст) == 'und fiel vor ihn hin. „Heda!“'


def test_након_речи():
    текст = 'und sprach "meine Stiefmutter"'
    assert ц(текст) == 'und sprach „meine Stiefmutter“'


def test_нова_линија1():
    текст = 'sagte:\n"Hallo, Mark"'
    assert ц(текст) == 'sagte:\n„Hallo, Mark“'


def test_нова_линија2():
    текст = '"erste lied."\n"zwiter lied."'
    assert ц(текст) == '„erste lied.“\n„zwiter lied.“'


def test_нова_линија3():
    текст = 'und sprach:\n"Mut heruet na myne Maegt"'
    assert ц(текст) == 'und sprach:\n„Mut heruet na myne Maegt“'


