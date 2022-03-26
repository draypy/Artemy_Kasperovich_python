def multiple_of_three(array: str) -> list or str:
    """
    The function gets a list and checks the numbers that are multiples of three
    :param array: List
    :return: list
    """
    try:
        list_numbers = [int(i) for i in array.split(',')]
        return [number for number in list_numbers if number % 3 == 0]
    except ValueError:
        return 'Неверный ввод'


if __name__ == '__main__':
    input_numbers = input('Введите числа через запятую. Например: 1,2,3\n')
    print(multiple_of_three(input_numbers))

