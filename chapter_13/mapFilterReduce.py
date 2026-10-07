from functools import reduce
# map Example

l = [1, 2, 3, 4, 5]

square = lambda x : x*x

sqList = map(square, l)
print(list(sqList))
# filter Example
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Example
def sum(a, b):
    return a + b

print(reduce(l))