from worker import Position

position = Position(
    name='Vasya',
    surname='Vasiev',
    position='Manager',
    income={'wage': 10000, 'bonus': 5000}
)

print(f'Name: {position.name}')
print(f'Surname: {position.surname}')
print(f'Position: {position.position}')
print(f'Full name: {position.get_full_name()}')
print(f'Total income: {position.get_total_income()}')
