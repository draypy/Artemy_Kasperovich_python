from typing import List, AnyStr, Optional
from decimal import Decimal, InvalidOperation


def multiple_of_three(array: AnyStr) -> Optional[List[Decimal]] or AnyStr:
    """
    The function gets a list and checks the numbers that are multiples of three
    :param array: List
    :return: list
    """
    try:
        list_numbers = [Decimal(i) for i in array.split(',')]
        return [number for number in list_numbers if number % 3 == 0]
    except InvalidOperation:
        return 'Неверный ввод'


if __name__ == '__main__':
    input_numbers = input('Введите числа через запятую. Например: 1,2,3\n')
    if isinstance(multiple_of_three(input_numbers), list):
        print(*multiple_of_three(input_numbers))
    print(multiple_of_three(input_numbers))


