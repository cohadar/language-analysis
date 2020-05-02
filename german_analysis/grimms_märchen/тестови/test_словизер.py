import pytest

from grimm.словизер import Словизер


def test_почетно():
    с = Словизер('trla', -2, -1)
    assert с.пре_два == -2
    assert с.претходно == -2
    assert с.тренутно == -2
    assert с.следеће == 't'
    assert с.за_два == 'r'
    assert с.индекс == -1


def test_напред():
    с = Словизер('trla', -2, -1)
    к = next(с)
    assert к == с.тренутно
    assert с.пре_два == -2
    assert с.претходно == -2
    assert с.тренутно == 't'
    assert с.следеће == 'r'
    assert с.за_два == 'l'
    assert с.индекс == 0


def test_напред2():
    с = Словизер('trla', -2, -1)
    next(с)
    next(с)
    assert с.пре_два == -2
    assert с.претходно == 't'
    assert с.тренутно == 'r'
    assert с.следеће == 'l'
    assert с.за_два == 'a'
    assert с.индекс == 1


def test_до_краја():
    с = Словизер('trla', -2, -1)
    next(с)
    next(с)
    next(с)
    next(с)
    assert с.пре_два == 'r'
    assert с.претходно == 'l'
    assert с.тренутно == 'a'
    assert с.следеће == -1
    assert с.за_два == -1
    assert с.индекс == 3


def test_преко_краја():
    с = Словизер('trla', -2, -1)
    next(с)
    next(с)
    next(с)
    next(с)
    with pytest.raises(StopIteration):
        next(с)


def test_преко_краја_default():
    с = Словизер('trla', -2, -1)
    next(с)
    next(с)
    next(с)
    next(с)
    assert -3 == next(с, -3)


def test_линија():
    с = Словизер('tr\nla', -2, -1)
    assert с.линија == 1
    next(с)
    next(с)
    assert с.линија == 1
    next(с)
    assert с.линија == 2

