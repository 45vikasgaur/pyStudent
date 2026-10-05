from functools import reduce
a = [111, 2, 32, 3, 32, 6556, 43, 34]

def greater(a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, a))