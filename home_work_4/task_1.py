def calculate_salary(hours, per_hour_rate, bonus=0):
    return (hours * per_hour_rate) + bonus


print(f'Without bonus: {calculate_salary(40, 10)}')
print(f'With bonus: {calculate_salary(40, 10, 40)}')
