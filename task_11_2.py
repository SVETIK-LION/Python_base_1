class ZeroError(Exception):
    default_message: str = 'Делить на ноль нельзя, запустите программу и введите другой делитель'

    def __str__(self):
        return self.default_message


dividend = int(input('Введите делимое: '))
divider = int(input('Введите делитель (НЕ равный 0): '))
try:
    if divider == 0:
        raise ZeroError()
    result = dividend/divider
    print(result)
except ZeroError as err:
    print(err)
