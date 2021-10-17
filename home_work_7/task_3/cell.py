class WrongCellsAmountError(Exception):
    pass


class Cell():
    def __init__(self, amount):
        self._amount = amount

    def __add__(self, cell):
        amount = self._amount + cell._amount
        return Cell(amount=amount)

    def __sub__(self, cell):
        if self._amount <= cell._amount:
            raise WrongCellsAmountError(
                f'Cells amount should be greater than {self._amount}'
            )

        amount = self._amount - cell._amount
        return Cell(amount=amount)

    def __mul__(self, cell):
        amount = self._amount * cell._amount
        return Cell(amount=amount)

    def __truediv__(self, cell):
        amount = round(self._amount / cell._amount)
        return Cell(amount=amount)

    @staticmethod
    def make_order(cell, cells_in_row):
        full_rows_count, last_row_size = divmod(cell._amount, cells_in_row)
        full_row = f'{"*" * cells_in_row}\n'
        full_rows = full_rows_count * full_row
        last_row = f'{"*" * last_row_size}\n' if last_row_size > 0 else ''
        result = full_rows + last_row
        return result

    def __str__(self):
        return f'Cells amount: {self._amount}'
