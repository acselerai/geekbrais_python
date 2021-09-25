number = input("Enter the number: ")


# First approach
digits = [int(digit) for digit in number]
digits.sort()
max_digit = digits[-1]

print("First approach max digit: ", max_digit)

# Second approach

counter = 0
max_value = 0

while counter < len(number):
    digit = int(number[counter])
    if max_value < digit:
        max_value = digit
    counter += 1

print("Second approach max digit: ", max_value)
