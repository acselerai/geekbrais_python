income = int(input("Enter the company income: "))
expences = int(input("Enter the company expences: "))

if income > expences:
    print("Everything is alright")
    profability = income - expences
    print(f"The profability is: {profability}")

    number_of_employees = int(input("Enter the number of employees: "))
    print(f"Employee's salary is: {(profability / number_of_employees):.2f}")
else:
    print("Everything is bad")
