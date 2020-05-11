import numpy as np

dxi = 0.1
xi = np.arange(0, np.pi/2, dxi)

dsin = (np.sin(xi[2:]) - np.sin(xi[:-2]))/(2*dxi)
print(dsin)

dcos = (np.cos(xi[2:]) - np.cos(xi[:-2]))/(2*dxi)
print(dcos)