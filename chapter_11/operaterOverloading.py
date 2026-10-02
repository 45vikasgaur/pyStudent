class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

    def __sub__(self, num):
        return self.n - num.n

    def __mul__(self, num):
        return self.n * num.n

    def __truediv__(self, num):
        return self.n / num.n

    def __floordiv__(self, num):
        return self.n // num.n

    def __mod__(self, num):
        return self.n % num.n


n = input("Enter a number: ")
num = Number(int(n))

s = input("Enter the operation you want to perform (+, -, *, /, %): ")

m = input("Enter another number: ")
num2 = Number(int(m))

if s == "+":
    print(f"The sum of {num.n} and {num2.n} is {num + num2}")

elif s == "-":
    print(f"The difference of {num.n} and {num2.n} is {num - num2}")
elif s == "*":
    print(f"The product of {num.n} and {num2.n} is {num * num2}")
elif s == "/":
    print(f"The division of {num.n} and {num2.n} is {num / num2}")

elif s == "//":
    print(f"The floor division of {num.n} and {num2.n} is {num // num2}")
elif s == "%":
    print(f"The remainder of {num.n} and {num2.n} is {num % num2}")
else:
    print("Invalid operation")
