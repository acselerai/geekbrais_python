ACCEPTABLE_SALARY = 20000.00

with open('task_3.txt', 'r') as file:
    employees_salary = dict(
        [line.split() for line in file if float(line.split()[1]) < 20000]
    )
    print('Employees with salary under 20000: ')
    for (employee, salary) in employees_salary.items():
        print(f'{employee}: {salary}')
