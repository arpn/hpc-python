def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


def better_fib(n):
    # Model solution uses memoization from functools which is
    # a nice solution. I'll make an uglier/hackier version.
    if n < 2:
        return n
    tick = 1
    arr = [1, 1]
    for i in range(2, n):
        tick = (tick + 1) % 2
        arr[tick] = sum(arr)
    return arr[tick]
