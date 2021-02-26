import math


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
        # Check if all values ar numbers
        if (
            not (type(x) == float or type(x) == int)
            or not (type(y) == float or type(y) == int)
            or not (type(z) == float or type(z) == int)
        ):
            raise TypeError
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, vector):
        # Check the correct type
        if type(vector) != Vector:
            raise TypeError

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
        # Check the correct type
        if type(vector) != Vector:
            raise TypeError

        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __sub__(self, vector):
        # Check the correct type
        if type(vector) != Vector:
            raise TypeError

        return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def __mul__(self, value):
        # Check the correct type
        if not (type(value) == Vector or type(value) == int or type(value) == float):
            raise TypeError
        if type(value) == Vector:
            return self.x * value.x + self.y * value.y + self.z * value.z
        else:
            return Vector(value * self.x, value * self.y, value * self.z)

    def cross_product(self, vector):
        """Calculates the crossproduct

        Args:
            vector (Vector): The vector to calculate the cross product with

        Returns:
            Vector: The crossproduct of the given vectors
        """
        # Check the correct type
        if type(vector) != Vector:
            raise TypeError
        x = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x
        return Vector(x, y, z)

    def length(self):
        """Returns the length of the Vector

        Returns:
            Vector: The length
        """
        return math.sqrt(
            math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2)
        )

    def angel(self, vector):
        """Calculate the angle between the given vectors

        Args:
            vector Vector: The vector to calculate the angel between

        Raises:
            TypeError: If the given value is not a Vector

        Returns:
            float: The angle
        """
        # Check the correct type
        if type(vector) != Vector:
            raise TypeError
        a = self * vector
        b = self.length() * vector.length()
        angel = math.acos(a / b)
        return round(math.degrees(angel), 5)
