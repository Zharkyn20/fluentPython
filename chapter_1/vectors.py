from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __str__(self):
        return 'Vector(x: {}, y: {})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(0, 0)
v2 = Vector(4, 3)
v_result = v1 + v2

print(abs(v_result))
print((bool(v_result)))
print(bool(v1))
print(v1 * 8)
print(v_result)
print(repr(v2))
