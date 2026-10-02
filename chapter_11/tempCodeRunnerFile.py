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
print(len(v1))