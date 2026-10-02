a = float(input("Enter number a:"))
o = input("Enter operator (+, -, *, /, //, %, **): ")
b = float(input("Enter number b:"))

if o == "+":
    print(a + b)
elif o == "-":
    print(a - b)
elif o == "*":
    print(a * b)
elif o == "/":
    print(a / b)
elif o == "//":
    print(a // b)
elif o == "%":
    print(a % b)
elif o == "**":
    print(a ** b)