from numba import njit


@njit()
def test(a, b):
    return a + b


print(test(1, 2))
