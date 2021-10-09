from random import randint

SEPARATOR = ' '

numbers = [randint(1, 101) for _el in range(1, 11)]

with open('task_5.txt', 'w') as file:
    file.write(SEPARATOR.join(str(number) for number in numbers))

with open('task_5.txt', 'r') as file:
    parsed_numbers = [int(num) for num in file.readline().split(SEPARATOR)]
    summary = sum(parsed_numbers)

print(f'Summary: {summary}')
