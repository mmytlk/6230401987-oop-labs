import math


class Circle:

    def __init__(self, x):
        self.x = x

    def area(self):
        return math.pi * math.pow(self.x, 2)

    def perimerter(self):
        return 2 * math.pi * self.x


if __name__ == '__main__':
    print(f"The circle with radius {Circle(3).x} has the area as {Circle(3).area():.2f}\n"
          f"and the perimeter as {Circle(3).perimerter():.2f}")
    print(f"The circle with radius {Circle(4).x} has the area as {Circle(4).area():.2f}\n"
          f"and the perimeter as {Circle(4).perimerter():.2f}")
