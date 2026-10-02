class Employee:
    language = "Python"  #this is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee("Harry", 1300000, "javaScript")
# harry.name = "vikas"
print(harry.name, harry.salary, harry.language)

# rohan = Employee()

# harry.language = "JavaScript"  #this is an instanc of attribute
# harry.getInfo()
# harry.getInfo()
# Emplyee.getInfo(harry) 

