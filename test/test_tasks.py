from Artemy_Kasperovich_python import Task1, Task2, Task3
from decimal import Decimal
import pytest


@pytest.mark.parametrize('number', ['9,1', 'q', '9', '7.1', '-1'])
def test_check_is_correct_task1(number):
    assert Task1.bigger_than_seven(number)


@pytest.mark.parametrize('name', ['Вячеслав', 'Brandon', 1])
def test_check_is_correct_task2(name):
    assert Task2.check_name(name)


@pytest.mark.parametrize('array', [('1,2,3,4'),
                                   ('1,3,9,7.1'),
                                   ('1,9,q'),
                                   ("1,")])
def test_check_is_correct_task3(array):
    assert Task3.multiple_of_three(array)
