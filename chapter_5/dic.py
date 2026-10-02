marks = {
    "Vikas": 100,
    "Shubham": 56,
    "Rohan": 23
}

# print(marks["Vikas"])
# print(marks.keys())
# print(marks.values())
# marks.update({"Rohan": 100})


marks.popitem("Rohan")
print(marks)