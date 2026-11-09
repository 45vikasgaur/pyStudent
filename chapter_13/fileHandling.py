with open("data.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Advanced Python")

with open("data.txt", "r") as file:
    data = file.read()

print(data)
