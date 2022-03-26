from typing import List, Optional
from decimal import Decimal, InvalidOperation


def multiple_of_three(array: List[Decimal]) -> Optional[List[Decimal]]:
    """
    The function gets a list and checks the numbers that are multiples of three
    :param array: List
    :return: list
    """
    return [number for number in array if number % 3 == 0]


try:
    list_numbers = [Decimal(i) for i in input('Введите числа через запятую. Например: 1,2,3\n').split(',')]
    print(*multiple_of_three(list_numbers))
except InvalidOperation:
    print('Неверный ввод')
