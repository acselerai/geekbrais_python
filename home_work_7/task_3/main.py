from cell import Cell, WrongCellsAmountError

cell_one = Cell(amount=4)
cell_two = Cell(amount=3)
cell_three = Cell(amount=2)
cell_four = Cell(amount=5)
cell_five = Cell(amount=3)
cell_six = Cell(amount=33)

result = (cell_one + cell_two - cell_three) * cell_four / cell_five

print(result)

print(f'Make order with size 3:\n{Cell.make_order(cell_six, 3)}')
print(f'Make order with size 4:\n{Cell.make_order(cell_six, 4)}')
print(f'Make order with size 5:\n{Cell.make_order(cell_six, 5)}')
print(f'Make order with size 6:\n{Cell.make_order(cell_six, 6)}')


try:
    cell_two - cell_one
except WrongCellsAmountError as err:
    print(err)
