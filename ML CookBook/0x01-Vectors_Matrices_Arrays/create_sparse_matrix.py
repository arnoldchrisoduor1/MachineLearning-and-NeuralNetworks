# Given a data with very few non-zero values we want to represent it efficiently.

import numpy as np
from scipy import sparse

matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])

# Creating a compressed sparse row (CSR) matrix.
matrix_sparse = sparse.csr_matrix(matrix)

print(matrix_sparse)