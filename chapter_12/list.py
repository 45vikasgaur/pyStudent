# l = [1, 2, 3, 4, 5]
# index = 0
# for item in l:
#     print(i)
#     index +=1


# for index, item in enumerate(l):
#     print(f"index is {index} and item is {item}")



numbers = [1, 2, 3, 4, 5]

squares = [x*x for x in numbers]
even = [x for x in numbers if x % 2 == 0]

print(squares)
print(even)