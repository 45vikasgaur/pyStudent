# a = int(input("Enter your number: "))
# if (a%2 == 0):
#     print("The number is even.")
# elif (a%2 != 0):
#     print("The number is odd.")
# else:
#     print("Invalid number entered.")


p1 = "make a lot of money"
p2 = "click now"
p3 = "buy minimum price"

massage = input("Enter the massage:")

if p1 in massage or p2 in massage or p3 in massage :
    print("this is spam massage!")
else:
    print("New massage for you:")