from typing import Optional
from decimal import Decimal, InvalidOperation


def bigger_than_seven(input_number: str) -> Optional[str]:
    """
    Function gets string, checks it. Return 'Привет' if number bigger than 7
    :param: str argument for validate
    :return: str or None
    """

    try:
        verified = Decimal(input_number)
        return 'Привет' if verified > 7 else ' '
    except InvalidOperation:
        return 'Нужно вводить число'


if __name__ == '__main__':
    number = input()
    print(bigger_than_seven(number))
