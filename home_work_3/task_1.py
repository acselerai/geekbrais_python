def division(arg_one, arg_two):
    try:
        return arg_one / arg_two
    except ZeroDivisionError:
        print('Division by zero is not allowed.')


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print(division(first_number, second_number))
