import numpy as np

data = np.loadtxt('xy-coordinates.dat')
print(data)

data[:, 1] += 2.5
np.savetxt('xy-coordinates-new.dat', data, fmt='%1.6f')
