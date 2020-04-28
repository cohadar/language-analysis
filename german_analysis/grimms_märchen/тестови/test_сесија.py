import random
from pathlib import Path
from тест.контејнер import Контејнер


def се():
    к = Контејнер()
    return к.сесија(тмпдир=Path('/tmp/www.google.com'))


def test_кеширање():
    с = се()
    урл = f'/tmp/www.google.com/{random.random()}'
    одговор = с.дај(урл)
    assert одговор.ок()
    assert not одговор.кеширан
    одговор = с.дај(урл)
    assert одговор.ок()
    assert одговор.кеширан

