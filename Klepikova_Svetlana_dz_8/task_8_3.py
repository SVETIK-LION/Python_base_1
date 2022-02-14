from functools import wraps


def type_logger(func):
    @wraps(func)
    def typer(*args, **kwargs):
        num = tuple(args or kwargs)
        for i in num:
            print(f'{calc_cube.__name__}({i}: {type(i)})')
    return typer


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5.5, 7, 'asr'))
