input = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def collect_greater_than_previous(input):
    return [
        input[index + 1]
        for index, element in enumerate(input[0:-2])
        if element < input[index + 1]
    ]


print(f'Result: {collect_greater_than_previous(input)}')
