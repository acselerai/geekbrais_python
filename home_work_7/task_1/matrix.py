class InvalidMatrixSizeError(Exception):
    pass


class Matrix():
    def __init__(self, matrix):
        self._matrix = matrix
        self._height = len(matrix)
        vectors_len = set([len(vector) for vector in matrix])
        if len(vectors_len) > 1:
            raise InvalidMatrixSizeError(
                'Matrix vectors should have the same size'
            )
        else:
            self._width = vectors_len.pop()

    def __add__(self, matrix):
        self.__validate_matrix(matrix)
        return Matrix(self.__concat(matrix._matrix))

    def __str__(self):
        return (
            '\n'.join(
                map(
                    lambda array: ' '.join([str(el) for el in array]),
                    self._matrix
                )
            )
        )

    def __concat(self, matrix):
        result = []
        for vector_index, vector in enumerate(self._matrix):
            vector_result = []
            for element_index, element in enumerate(vector):
                vector_result.append(
                    element + matrix[vector_index][element_index]
                )
            result.append(vector_result)

        return result

    def __validate_matrix(self, matrix):
        if matrix._height != self._height:
            self.raise_same_size_error()
        elif matrix._width != self._width:
            self.raise_same_size_error()

    def raise_same_size_error(self):
        raise InvalidMatrixSizeError(
            'Matrix should have the same size'
        )
