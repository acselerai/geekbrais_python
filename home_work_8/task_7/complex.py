class ComplexNumber():
    def __init__(self, number_one, number_two):
        self._number_one = number_one
        self._number_two = number_two

    def __add__(self, complex_number):
        return ComplexNumber(
            number_one=self._number_one + complex_number._number_one,
            number_two=self._number_two + complex_number._number_two
        )

    def __mul__(self, complex_number):
        return ComplexNumber(
            number_one=self._number_one * complex_number._number_one - self._number_two * complex_number._number_two,
            number_two=self._number_one * complex_number._number_two + self._number_two * complex_number._number_one,
        )

    def __str__(self):
        return f'complex({self._number_one}, {self._number_two})'
