def check_name(name: str) -> str:
    return 'Привет, Вячеслав' if name == 'Вячеслав' else 'Нет такого имени'


print(check_name(input('Введите имя: ')))
