a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if (b == 0):
    raise ZeroDivisionError("Division by zero is not allowed.")
    
else:
    print(f"the division of {a} and {b} is {a/b} ")
    