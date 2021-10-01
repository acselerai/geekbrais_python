elements = [1, 'string', True, 1.0]


def check_elements_type(enuberable):
    for index, element in enumerate(enuberable):
        print(f'The type of {index + 1} element is {type(element)}')


check_elements_type(elements)
