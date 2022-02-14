from functools import wraps


def val_checker(check):
    def _decor(func):
        @wraps(func)
        def wrapper(x):
            if check(x) == True:
                return func(x)
            else:
                raise ValueError(f'wrong val: {x}')
        return wrapper
    return _decor


check = lambda x: x > 0
@val_checker(check)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    try:
        print(calc_cube(5))
        print(calc_cube('ss'))
    except (ValueError, TypeError) as err:
        print(err)
