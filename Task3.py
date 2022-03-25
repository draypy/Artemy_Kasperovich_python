def multiple_of_three(array: list) -> list:
    return [number for number in array if number % 3 == 0]


try:
    list_numbers = [int(i) for i in input('Введите числа через запятую. Например: 1,2,3\n').split(',')]
    print(multiple_of_three(list_numbers))
except ValueError:
    print('Неверный ввод')
