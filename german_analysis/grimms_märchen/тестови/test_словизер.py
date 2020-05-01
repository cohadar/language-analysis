import pytest

from grimm.словизер import Словизер


def test_почетно():
    с = Словизер('trla')
    assert с.претходно == -1
    assert с.тренутно == 't'
    assert с.следеће == 'r'
    assert с.индекс == 0


def test_напред():
    с = Словизер('trla')
    с.напред()
    assert с.претходно == 't'
    assert с.тренутно == 'r'
    assert с.следеће == 'l'
    assert с.индекс == 1


def test_до_краја():
    с = Словизер('trla')
    с.напред()
    с.напред()
    с.напред()
    assert с.претходно == 'l'
    assert с.тренутно == 'a'
    assert с.следеће == -1
    assert с.индекс == 3


def test_преко_краја():
    с = Словизер('trla')
    с.напред()
    с.напред()
    с.напред()
    with pytest.raises(StopIteration):
        с.напред()

