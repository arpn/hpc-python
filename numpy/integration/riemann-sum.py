import numpy as np


def riemann(n):
    dx = np.pi/2/(n-1)
    x = np.linspace(0.0, np.pi/2, n)
    xmid = (x[:-1] + x[1:])/2
    return np.sum(np.sin(xmid))*dx


print(riemann(5))
print(riemann(10))
print(riemann(20))
print(riemann(100))