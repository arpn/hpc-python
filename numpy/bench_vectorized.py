import numpy as np

def test_loop():
    arr = np.arange(1000)
    dif = np.zeros(999, int)
    for i in range(1, len(arr)):
        dif[i-1] = arr[i] - arr[i-1]

def test_vectorized():
    arr = np.arange(1000)
    dif = arr[1:] - arr[:-1]
