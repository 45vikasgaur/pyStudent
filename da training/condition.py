# number = int(input("Enter the number:"))
# if number > 0:
#     print("positive number")
# elif number < 0:
#     print("negative number")
# else:
#     print("zero")


# marks = int(input("Enter marks:"))
# if marks >= 40:
#     print("Pass")
# else:
#     print("Fail")



# -------------------------conditional----------------

# marks = float(input("Enter the marks: "))
# if marks>=90:
#     print("Grade A")
# elif marks>=75:
#     print("Grade B")
# elif marks>=60:
#     print("Grade C")
# elif marks>=40:
#     print("Grade D")
# else:
#     print("Fail")      


# # ------------------- calculator----------------

# num1 = float(input("Enter the first number: "))
# op = input("Enter the operator: ")
# num2 = float(input("Enter the second number: "))

# if op == '+':
#     result = num1+num2
# elif op == '-':
#     result = num1-num2
# elif op == '*':
#     result = num1*num2
# elif op == '/':
#     if num1 != 0:
#         result = num1/num2
#     else:
#         result = "Cannot divide by zero"
# else:
#     result = "Invalid op"
# print("Result is: ", result)



# #    ------- ATM wuthdrawal---------

# balance = 5000
# amount = float(input("Enter the amount: "))
# if amount <=0:
#     print("Invalid amount")
# elif amount > balance:
#     print("insufficient balance")
# else:
#     balance = balance - amount
#     print("withdrawal successful!")




# #   --------  COLLege student -------

# marks = float(input("Enter your marks: "))
# en_pass = True
# if marks>=75:
#     if en_pass:
#         print("Eligibal for admision")
#     else:
#         print("Not eligible for admision")
# else:
#     print("marks requred not setisfied")






# # --------login system--------

# username_in = input("Enter your User Name: ")
# username = "45vikasgaur"
# password = "vikas45gaur"

# if username_in == username:
#     password_in = input("Enter your Password:")
#     if password_in == password:
#         print("Welcome to page")
#     else:
#         print("wrong password")
# else:
#     print("User Name is not found")





# --------AND OR NOT Logical operator--------

age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

if age>=18 and  age <= 30 and marks>=70:
    print("You are eligible for admission")
else:
    print("you are not eligible for admission")


#     --------or--------
day = input("Enter Day: ")
day1 = saturday
day2 = sunday

if day1==day or day==day2:
    print("weekend")
else:
    print("workingday")



