class Employee: #base class
    def show(self):
        print(f"The nameus {self.name} and the salary is {self.salary}")

class Coder:
    language = "python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee, Coder): #derived class
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()