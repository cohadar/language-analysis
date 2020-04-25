import random
from тест.контејнер import Контејнер


def се():
    к = Контејнер()
    return к.сесија()


def test_кеширање():
    с = се()
    урл = f'www.google.com/{random.random()}'
    одговор = с.дај(урл)
    assert одговор.ок()
    assert not одговор.кеширан
    одговор = с.дај(урл)
    assert одговор.ок()
    assert одговор.кеширан

