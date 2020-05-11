#!/bin/bash

echo "Python"
python -m timeit -s "from py_module import subtract" "subtract(3, 4)"

echo "Cython"
python -m timeit -s "from cyt_module import subtract" "subtract(3, 4)"
