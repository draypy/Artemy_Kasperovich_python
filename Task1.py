def bigger_than_seven(number: int) -> str:
    if int(number) > 7:
        return 'Привет'


try:
    print(bigger_than_seven(int(input('Введите число: '))))
except ValueError:
    print('Нужно вводить число')
