# Common operation in linear algebra where the columns and rows are swapped.

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Transposing the matrix.
print(matrix.T)

# Transposing a vector is converting a row vector into a column vector.