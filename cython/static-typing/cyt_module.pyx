def subtract(int x, int y):
    cdef int result
    result = x - y
    return result

# If args are floats, then they are cast to integers automatically
# If args were declared to be float, a compilation error occurs