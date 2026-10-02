# day = input("Enter a day of the week: ")
# if day.lower() == "monday":
#     print("Working day!")
# elif day.lower() == "tuesday":
#     print("Working day!")
# elif day.lower() == "wednesday":
#     print("Working day!")
# elif day.lower() == "thursday":
#     print("Working day!")
# elif day.lower() == "friday":
#     print("Working day!")
# elif day.lower() == "saturday":
#     print("It's Saturday! Weekend!")
# elif day.lower() == "sunday":
#     print("It's Sunday! Rest and recharge!")
# else:
#     print("Invalid day entered.")



a = int(input("Enter your age: "))

if a > 18 and a <= 150:
    print("You are eligible to vote.")
elif a <= 0 or a > 150:
    print("Invalid age entered.")
elif a == 0:
    print("You are entering 0 which is not a valid age.")
else:
    print("You are not eligible to vote.")

print("End of program.")