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


def test_најчешћи_наводници():
    текст = 'sagte: "Hallo Mann." Er'
    assert ц(текст) == 'sagte: „Hallo Mann.“ Er'


def test_најчешћи_затворено_зарез():
    текст = 'sagte: "Hallo Mann," Er'
    assert ц(текст) == 'sagte: „Hallo Mann,“ Er'


def test_најчешћи_затворено_хип():
    текст = 'sagte: "Hallo Mann," -'
    assert ц(текст) == 'sagte: „Hallo Mann,“ -'


def test_најчешћи_затворено_узвик():
    текст = 'sagte: "Hallo Mann!" Er'
    assert ц(текст) == 'sagte: „Hallo Mann!“ Er'


def test_најчешћи_затворено_питање():
    текст = 'sagte: "Hallo Mann?" Er'
    assert ц(текст) == 'sagte: „Hallo Mann?“ Er'


def test_најчешћи_затворено_питање_минус():
    текст = 'sagte: "Hallo Mann?" -'
    assert ц(текст) == 'sagte: „Hallo Mann?“ -'


def test_најчешћи_затворено_питање_хип():
    текст = 'sagte: "Hallo Mann?" –'
    assert ц(текст) == 'sagte: „Hallo Mann?“ –'


def test_затворен_нл1():
    текст = 'sagte: "Hallo Mann."\nEr'
    assert ц(текст) == 'sagte: „Hallo Mann.“\nEr'


def test_затворен_нл2():
    текст = 'sagte: "Hallo Mann."\n\n'
    assert ц(текст) == 'sagte: „Hallo Mann.“\n\n'


def test_затворен_нл3():
    текст = 'sagte: "Hallo Mann."\n"Er '
    assert ц(текст) == 'sagte: „Hallo Mann.“\n„Er '


def test_сумњиво_ал_ради_затварање():
    текст = 'sagte: "Hallo Mann " Er'
    assert ц(текст) == 'sagte: „Hallo Mann “ Er'


def test_личи_на_затварање_а_није():
    текст = 'Und Gretel sagte:" Er'
    with pytest.raises(ЦитатГрешка) as грешка:
        ц(текст)
    assert грешка.value.args[0] == 'џ:" џ'


def test_отварање_након_интерпункције1():
    текст = 'sagte: "Hallo Mann." Er'
    assert ц(текст) == 'sagte: „Hallo Mann.“ Er'


def test_отварање_након_интерпункције2():
    текст = 'dann, "Hallo Mann." Er'
    assert ц(текст) == 'dann, „Hallo Mann.“ Er'


def test_отварање_након_интерпункције3():
    текст = 'dann - "Hallo Mann." Er'
    assert ц(текст) == 'dann – „Hallo Mann.“ Er'


def test_отварање_након_интерпункције4():
    текст = 'dann. "Hallo Mann." Er'
    assert ц(текст) == 'dann. „Hallo Mann.“ Er'


def test_отварање_без_интерпункције1():
    текст = 'dann "Hallo Mann." Er'
    assert ц(текст) == 'dann „Hallo Mann.“ Er'


def test_отварање_без_интерпункције2():
    текст = 'dann "Hallo, Mann." Er'
    assert ц(текст) == 'dann „Hallo, Mann.“ Er'


def test_отварање_након_интерпункције5():
    текст = 'sagte: "Hallo, Mann." Er'
    assert ц(текст) == 'sagte: „Hallo, Mann.“ Er'


def test_отварање_након_интерпункције6():
    текст = 'dann - "Hallo, Mann." Er'
    assert ц(текст) == 'dann – „Hallo, Mann.“ Er'


def test_отварање_након_интерпункције7():
    текст = 'dann. "Hallo, Mann." Er'
    assert ц(текст) == 'dann. „Hallo, Mann.“ Er'


def test_отварање_након_интерпункције8():
    текст = 'sagte: "Hallo! Mann." Er'
    assert ц(текст) == 'sagte: „Hallo! Mann.“ Er'


def test_отварање_након_нл1():
    текст = 'sagte: "Hallo Mann."\n"Er '
    assert ц(текст) == 'sagte: „Hallo Mann.“\n„Er '


def test_отварање_након_нл2():
    текст = '\n\n"Er ist." Sie'
    assert ц(текст) == '\n\n„Er ist.“ Sie'


def test_отварање_након_нл3():
    текст = 'sagte:\n"Er ist." Sie'
    assert ц(текст) == 'sagte:\n„Er ist.“ Sie'


def test_отварање_након_нл4():
    текст = '\n\n"Er, ist." Sie'
    assert ц(текст) == '\n\n„Er, ist.“ Sie'




