import json

student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    data = json.load(file)

print(data)