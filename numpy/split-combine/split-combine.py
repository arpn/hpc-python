import numpy as np

x = np.random.randint(0, 10, (8, 8))
print(x)
print()

y1, y2 = np.split(x, 2, axis=0)
print(y1)
print()
print(y2)
print()

z = np.concatenate((y1, y2))
print(z)

y1, y2 = np.split(x, 2, axis=1)
print(y1)
print()
print(y2)
print()

z = np.concatenate((y1, y2), axis=1)
print(z)
