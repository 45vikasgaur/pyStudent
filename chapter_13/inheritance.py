class Employee: #base class
    def show(self):
        print(f"The nameus {self.name} and the salary is {self.salary}")

# class Programmer:
#     comany = "ITC Infotech"
#     def show(self):
#         print(f"The nameus {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The name is {`self.name} and he is good with {self.language} language")
    
    
class Programmer(Employee): #derived class
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company) 


#single inheritance 
# multiple inheritance 
# multilevel inheritence