from matrix import Matrix, InvalidMatrixSizeError

first_matrix = Matrix(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)

second_matrix = Matrix(
    [
        [6, 5, 4],
        [3, 2, 1]
    ]
)

print(first_matrix, '\n')
print(second_matrix, '\n')
print(first_matrix + second_matrix)

try:
    invalid_matrix_one = Matrix(
        [
            [1, 2, 3, 4],
            [1],
            [1, 2, 3]
        ]
    )
    first_matrix + invalid_matrix_one
except InvalidMatrixSizeError as err:
    print(err)

try:
    invalid_matrix_two = Matrix(
        [
            [1, 2],
            [3, 4]
        ]
    )
    first_matrix + invalid_matrix_two
except InvalidMatrixSizeError as err:
    print(err)
