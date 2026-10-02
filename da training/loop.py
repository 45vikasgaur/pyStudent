# print("stop condition")
# for i in range(5):  
#     print(i)

# print("start + stop")
# for i in range(1,6):
#     print(i)

# print("stapping condition")
# for i in range(2,11,2):
#     print(i)


print("even")
for i in range(0,21,2):
    print(i)

print("odd")
for i in range(1,20,2):
    print(i)

print("dividible")
for i in range(3,33,3):
    print(i)

print("multiple")
for i in range(5,51,5):
    print(i)

print("square")
for i in range(1,6):
    print(i,i**2)

print("cube")
for i in range(1,6):
    print(i,i**3)

print("Sum of Natural number ")

n = int(input("Enter natural number"))
total = 0
for i in range(1,n+1):
    total +=i
    print("sum = ",total)


nn = int(input("Enter number :"))
for i in range(1,11):
    print(nn,"x", i, "=", nn*i)
