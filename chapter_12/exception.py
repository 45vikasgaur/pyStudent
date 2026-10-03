try:
    a = int(input("Enter a number: ") )
    print(a)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
except Exception as e:
    print(f"Error: {e}")

print("goodbye")