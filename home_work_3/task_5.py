EXIT = '*'


def request_numbers_from_user():
    return input('Enter numbers separated by space: ')


def increment_sum(value, sum):
    return sum + value


def convert_string_to_numbers(input_string, separator=' '):
    return sum(
        [int(element) for element in input_string.split(separator)]
    )


def default_error_handler():
    return 0


def wrap_error(func, handler=default_error_handler):
    try:
        return func()
    except ValueError:
        return handler()


def extract_numbers(input_string):
    return input_string.split(EXIT)[0].strip()


def print_summary(summary):
    print('Summary is: ', summary)


def start():
    print('Type "*" to quit')

    exit = False
    sum = 0

    while exit is not True:
        user_input = request_numbers_from_user()
        if user_input.count(EXIT):
            exit = True
        sum = increment_sum(
            wrap_error(
                lambda: convert_string_to_numbers(
                    extract_numbers(user_input)
                )
            ),
            sum
        )
        print_summary(sum)


start()
