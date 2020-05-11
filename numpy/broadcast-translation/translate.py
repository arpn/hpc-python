import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('points_circle.dat')
plt.plot(data[:, 0], data[:, 1], 'o')
plt.savefig('original.png')
plt.close()

translated = data + np.array((2.1, 1.1))
plt.plot(translated[:, 0], translated[:, 1], 'o')
plt.savefig('translated.png')
plt.close()
