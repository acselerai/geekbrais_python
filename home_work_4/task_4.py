input =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [element for element in input if input.count(element) == 1 ]

print(f'Result: {result}')
