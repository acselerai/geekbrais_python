# First approach

def pow_first_implementation(first_number, second_number):
    return first_number ** second_number


print('First implementation: ', pow_first_implementation(1.3, 4))

# Second implementation


def pow_second_implementation(first_number, second_number):
    for x in range(second_number):
        first_number *= first_number

    return first_number


print('Second implementation: ', pow_first_implementation(1.3, 4))
