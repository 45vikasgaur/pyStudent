print("Hello, World!")
name = "vikas" 
age = 20
country = "India"

print(type(name))
print(type(age))
print(type(country))

# name = input("What is your name? ")
# print(f"Nice to meet you, {name}!")


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
sum = number1 + number2
print(f"The sum of {number1} and {number2} is {sum}.")

a = float(input("Enter the amount: "))
r = float(input("Enter the rate of interest (in %): "))
t = float(input("Enter the time (in years): ")) 

si = (a * r * t) / 100

print(f"The simple interest is: {si}")


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")

name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter student course: ")
marks = float(input("Enter student marks: "))
print(f"Student Name: {name}")
print(f"Student Age: {age}")
print(f"Student Course: {course}")
print(f"Student Marks: {marks}")
 
