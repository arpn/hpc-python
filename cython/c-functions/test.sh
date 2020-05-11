#!/bin/bash

echo "Python"
python -m timeit -s "from fib_py import fibonacci" "fibonacci(30)"

echo "Cython"
python -m timeit -s "from fib import fibonacci" "fibonacci(30)"

echo "Better python"
python -m timeit -s "from fib_py import better_fib" "better_fib(30)"
