class Animals:
    pass

class pets(Animals):
    pass

class Dog(pets):
    @property
    def bark(self):
        print("Bow Bow!")

d = Dog()
d.bark



# ------problem2 ---------


class Employee:
    salary = 10000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

e = Employee()
print(e.salaryAfterIncrement)



# -----problem 3-----



class Employee:
    salary = 10000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1) * 100

e = Employee()
print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 12000
print(e.increment)

# --------problem 4 ---------

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
        real_part = self.r + c2.r - self.i * c2.i
        imag_part = self.i + c2.i + self.i * c2.r
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1, 2)
c2 = Complex(2, 3)
print(c1 + c2)
print(c1*c2)



# -------problem 5 ---------

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v2):
        result = Vector(self.x + v2.x, self.y + v2.y, self.z + v2.z)
        return result

    def __mul__(self, v2):
        # Placeholder for vector multiplication (dot product)
        result = self.x * v2.x + self.y * v2.y + self.z * v2.z
        return result

    def __str__(self):
        return f"Vector({self.x}i, {self.y}j, {self.z}k)"

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)
print(v1 + v2)
print(v1 * v2) 

print(v1 + v3)
print(v1 * v3)


# --------problem 6 ---------     

class Vector:
    def __init__(self, l):
        self.x, self.y, self.z = l

    def __add__(self, v2):
        result = Vector(self.x + v2.x, self.y + v2.y, self.z + v2.z)
        return result

    def __mul__(self, v2):
        # Placeholder for vector multiplication (dot product)
        result = self.x * v2.x + self.y * v2.y + self.z * v2.z
        return result

    def __str__(self):
        return f"Vector({self.x}i, {self.y}j, {self.z}k)"

    def __len__(self):
        return 3

v1 = Vector([1, 2, 3])
print(len(v1))  # Output: 3