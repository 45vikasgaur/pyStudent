class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Vikas", 120000, 272152)
print(p.name, p.salary, p.pin, p.company)
s = Programmer("sachin", 120000, 272152)
print(s.name, s.salary, s.pin, s.company)