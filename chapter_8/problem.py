# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))
# c = int(input("Enter a third number: "))

# def greet():
#     if a>b and a>c:
#         print("a is a bigest number ", a)
#     elif b>a and b>c:
#         print("b is a bigest number.", b)
#     else:
#         print("c is a bigest number. ", c)

# greet()



# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter temperature in F: " ))
# c = f_to_c(f)

# print(f"{round(c, 2)}°C")



# def sum(n):
#     if n==1:
#         return 1
#     return sum(n -1) + n

# print(sum(5))



# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)


# pattern(3)



# def inch_to_cm(inch):
#     return inch* 2.54

# a = int(input("Enter the value in inch: "))
# print(f"The value in cm is {inch_to_cm))

# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# l = ["Vikas", "Sachin", "abhay", "yogesh"]
# print(rem(l,"a"))


def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i}= {n*i}")
multiply(5)