def type_logger(func):
    def typer(num):
        return f'{num}: {type(num)}'
    return typer


@type_logger
def calc_cube(x):
   return x ** 3


print(calc_cube(5))
