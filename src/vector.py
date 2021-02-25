class Vector:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, vector):
        if self.x == vector.x and self.y == vector.y and self.z == vector.z:
            return True
        else:
            return False

    def __str__(self):
        return f"({self.x}|{self.y}|{self.z})"

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)


if __name__ == "__main__":
    print(str(Vector(1, 2, 3)))
