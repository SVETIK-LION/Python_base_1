class DigitError(ValueError):
    default_message = 'это не число, введите другое значение или "stop"'


numbers = []
while True:
    try:
        num = input('Введите число (чтобы заверщить список введите "stop"): ')
        if num == 'stop':
            break
        if not num.isdigit():
            raise DigitError(num)
        numbers.append(int(num))
    except DigitError as err:
        print(f'{err} - {DigitError.default_message}')

print(numbers)
