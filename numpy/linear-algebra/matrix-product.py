import numpy as np
import numpy.random as npr

A = npr.random((2, 2))
A = A + A.T
B = npr.random((2, 2))
B = B + B.T

C = A.dot(B)
print(C)

print('Eigenvalues = ', np.linalg.eigvals(C))