import math

def fermactor(n):
    e = list(set(reduce(list.__add__,([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))
    e.sort()
    f = (e[-2] - e[-3])
    g = list(set(reduce(list.__add__, ([i, f // i] for i in range(1, int(f ** 0.5) + 1) if f % i == 0))))
    g.sort()
    return [int(math.sqrt((g[-2]**2 + n))), g[-2]]

