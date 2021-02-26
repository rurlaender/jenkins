class Vector:
    """
    Object class representing a 3d vector object
    """

    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        """
        Initializes a new 3D vector object
        """
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, vector):
        if self.x == vector.x and self.y == vector.y and self.z == vector.z:
            return True
        else:
            return False

    def __str__(self):
        """
        Formats the vactor for printing
        """
        return f"({self.x}|{self.y}|{self.z})"

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def cross_product(self, vector):
        """Calculates the crossproduct

        Args:
            vector (Vector): The vector to calculate the cross product with

        Returns:
            Vector: The crossproduct of the given vectors
        """
        x = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x
        return Vector(x, y, z)


if __name__ == "__main__":
    print(str(Vector(1, 2, 3)))
