try:
    with open("1.txt", "r") as file:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open("2.txt", "r") as file:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open("3.txt", "r") as file:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}") 


print("good morning")

