def check_name(name: str) -> str:
    """
    Function gets string, and compare with "Вячеслав".
    :param name: str
    :return: str
    """
    return 'Привет, Вячеслав' if name == 'Вячеслав' else 'Нет такого имени'


if __name__ == '__main__':
    print(check_name(input('Введите имя: ')))
