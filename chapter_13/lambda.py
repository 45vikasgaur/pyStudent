# def square(n):
#     return n*n


# square =  lambda x: x*x
# #  lambda function is use for expression, it can take any number of arguments but can only have one expression.
# print(square(5))


from functools import reduce

numbers = [1, 2, 3, 4, 5]

square = list(map(lambda x: x*x, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda x, y: x + y, numbers)

print(square)
print(even)
print(total)