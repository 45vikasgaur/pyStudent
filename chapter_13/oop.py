class Employee:

    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def annual_salary(self):
        return self.salary * 12

    @classmethod
    def company_name(cls):
        return cls.company

    @staticmethod
    def greet():
        print("Welcome!")

e = Employee("Rahul", 30000)

print(e.annual_salary)
print(Employee.company_name())
Employee.greet()