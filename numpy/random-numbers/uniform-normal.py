import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

print('Uniform distribution:')
x = npr.random(1000)
print('mean =', np.mean(x))
print('std =', np.std(x))
plt.subplot(1, 2, 1)
plt.hist(x)
plt.title('Unif(0,1)')

print('Beta(2,5):')
x = npr.beta(2, 5, 1000)
print('mean =', np.mean(x))
print('std =', np.std(x))
plt.subplot(1, 2, 2)
plt.hist(x)
plt.title('Beta(2,5)')

plt.savefig('histograms.png')
