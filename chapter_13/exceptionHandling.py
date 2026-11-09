try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))

    print(a / b)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program finished")