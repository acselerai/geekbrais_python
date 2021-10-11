from itertools import count, cycle

END_OF_SEQUENCE = 10


def generate_sequence(start=0, end=END_OF_SEQUENCE):
    for element in count(start):
        if element == end + 1:
            break
        else:
            print(element)


print('Start of generating the sequence: ')
generate_sequence(3, end=10)


ITERATIONS_LIMIT = 10

list_to_repeat = [1, 2, 3, 4, 5, 6]


def repeat_sequence(input_list, iterations=ITERATIONS_LIMIT):
    iterations_count = 0
    for element in cycle(input_list):
        if iterations_count == iterations:
            break
        else:
            print(element)
            iterations_count += 1


print('Start of repeating the sequesnce: ')
repeat_sequence(list_to_repeat)
