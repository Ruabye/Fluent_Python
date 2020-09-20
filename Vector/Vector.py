from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        #"+"
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __abs__(self):
        #"abs()"
        return hypot(self.x, self.y)

    def __repr__(self):
        #"print()"
        return "Vector(%r, %r)"%(self.x, self.y)

    def __mul__(self, other):
        #"*"
        return Vector(self.x * other.x, self.y * other.y)

    def __bool__(self):
        #"bool()"
        return bool(abs(self))

if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(2, 3)

    print(v1 + v2)
    print(v1 * v2)
    print(abs(v1), abs(v2))
    print(bool(Vector()))