import pytest

from grimm.словизер import Словизер


def test_почетно():
    с = Словизер('trla')
    assert с.претходно == -1
    assert с.тренутно == -1
    assert с.следеће == 't'
    assert с.индекс == -1


def test_напред():
    с = Словизер('trla')
    к = next(с)
    assert к == с.тренутно
    assert с.претходно == -1
    assert с.тренутно == 't'
    assert с.следеће == 'r'
    assert с.индекс == 0


def test_напред2():
    с = Словизер('trla')
    next(с)
    next(с)
    assert с.претходно == 't'
    assert с.тренутно == 'r'
    assert с.следеће == 'l'
    assert с.индекс == 1


def test_до_краја():
    с = Словизер('trla')
    next(с)
    next(с)
    next(с)
    next(с)
    assert с.претходно == 'l'
    assert с.тренутно == 'a'
    assert с.следеће == -1
    assert с.индекс == 3


def test_преко_краја():
    с = Словизер('trla')
    next(с)
    next(с)
    next(с)
    next(с)
    with pytest.raises(StopIteration):
        next(с)


def test_преко_краја_default():
    с = Словизер('trla')
    next(с)
    next(с)
    next(с)
    next(с)
    assert -2 == next(с, -2)


def test_линија():
    с = Словизер('tr\nla')
    assert с.линија == 1
    next(с)
    next(с)
    assert с.линија == 1
    next(с)
    assert с.линија == 2

