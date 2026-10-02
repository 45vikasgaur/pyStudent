# name = input("Enter your name: ")
# date = int(input("Enter the date in year: "))
# print(f'''Dear {name},
# you are selected !
# {date}''')


letter = '''Dear <|name|>,
You are selected !
<|date|>'''

print(letter.replace("<|name|>", "vikas").replace("<|date|>", "2023-06-20"))


name = "there are many people in the world" #string is a immutable data type in python. once a string is created it cannot be modified
print(name.find("people"))
