class MyZeroDevisionError(Exception):
    pass


def division(number, by):
    if by == 0:
        raise MyZeroDevisionError(
            'Division by zero is not allowed'
        )
    return number / by


try:
    print(f'4 / 2 = {division(4, 2)}')
    print(f'4 / 0 = {division(4, 0)}')
except MyZeroDevisionError as err:
    print(err)
