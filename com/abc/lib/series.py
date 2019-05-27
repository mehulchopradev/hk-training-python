# module -> series
# library of functions (function definitions)

def get_fibo_series(n):
    result = ''
    a, b = 0, 1
    result += str(a) + '\n' + str(b) + '\n' # str converts from any type to string
    # as can concatenate a str with a str only
    for v in range(1, n - 1):
        c = a + b
        result += str(c) + '\n'
        a, b = b, c
    return result


def get_even_series(n):
    result = ''
    for i in range(0, n + 1, 2): # third parameter in range is the step size
        result += str(i) + '\n'
    return result