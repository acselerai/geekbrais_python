from math import factorial

EDGE_NUMBER = 10


def fact(edge_number=EDGE_NUMBER):
    for number in range(1, edge_number + 1):
        yield factorial(number)


print('Start calculating factorials: ')
for calculated_factorial in fact(9):
    print(calculated_factorial)
