from functools import wraps


def val_checker(num=4):
    # @wraps(func)
    def check_ext(func):
        def check_int(*args, **kwargs):
            try:
                if num > 0:
                    return calc_cube(num)
                else:
                    # if num <= 0 or str(num).isdigit() == False:
                    raise ValueError(f'Wrong val: {num}')
            except ValueError as err:
                return err
        return check_int
    return check_ext



@val_checker(num=10)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))