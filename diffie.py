import math

def mod_exp(x, y, N):
    # Base case: x^0 mod N = 0
    if (y == 0):
        return 1
    z = mod_exp(x, math.floor(y/2), N)
    if (y % 2 == 0):
        return (z**2) % N
    else:
        return (x * (z**2)) % N

