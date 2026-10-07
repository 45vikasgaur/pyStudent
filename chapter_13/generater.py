def numbers(n):
    for i in range(n):
        yield i

for num in numbers(5):
    print(num)