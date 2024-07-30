# Selecting elements in a vector or a matrix.

import numpy as np

# create a row vector.
vector = np.array([1, 2, 3, 4, 5, 6 ])

# Create matrix.
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# selecting the third element of the vector.
vector[2]

# Selecting the second row, second column
matrix[1, 1]