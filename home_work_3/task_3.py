def sum_of_two_max_values(first, second, third):
    numbers = [first, second, third]
    first_max_number = max(numbers)
    numbers.remove(first_max_number)
    second_max_number = max(numbers)
    print(f'{first_max_number + second_max_number}')


sum_of_two_max_values(12, 13, 11)
