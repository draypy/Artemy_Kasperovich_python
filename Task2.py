def check_name(name: str) -> str:
    """
    Function gets string, and compare with "Вячеслав".
    :param name: str
    :return: str
    """
    check = 'Вячеслав'
    return f'Привет, {check}' if name == check else 'Нет такого имени'


print(check_name(input('Введите имя: ')))
