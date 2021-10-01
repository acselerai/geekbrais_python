user_input = input("Enter the numbers separated by commas: ")

numbers = list(
    user_input.split(',')
)

list_size = len(numbers)
element_without_pair = list_size - 1

result = []
for index, element in enumerate(numbers):
    if index == element_without_pair and list_size % 2 != 0:
        result.append(element)
    elif index % 2 == 1:
        result.append(element)
        result.append(numbers[index - 1])
    else:
        continue


print(f'Result: {result}')
