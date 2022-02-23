from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise ValueError('fail initialization matrix')

    def __str__(self):
        str_matr = ''
        for elem in self.matrix:
            str_elem = f'| {" ".join(map(str, elem))} |\n'
            str_matr += str_elem
        return  str_matr

    def __add__(self, other):
        lst_matr = []
        for i in range(len(self.matrix)):
            elem = []
            for j in range(len(self.matrix[i])):
                new_elem = self.matrix[i][j] + other.matrix[i][j]
                elem.append(new_elem)
            lst_matr.append(elem)
        lst_matr = Matrix(lst_matr)
        return lst_matr

if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
