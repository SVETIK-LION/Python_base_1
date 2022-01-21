def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    if number in (11, 12, 13, 14):
        result = number, 'процентов'
    elif number % 10 == 1:
        result = number, 'процент'
    elif (number % 10 == 2) or (number % 10 == 3) or (number % 10 == 4):
        result = number, 'процента'
    else:
        result = number, 'процентов'
    return result

for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(*transform_string(n))