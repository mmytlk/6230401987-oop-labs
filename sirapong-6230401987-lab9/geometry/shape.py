from abc import *
import random


class Shape(ABC):
    @abstractmethod
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    num_circles = 0

    def __init__(self, colors, radius):
        super().__init__(colors)
        type(self).num_circles += 1
        self.radius = radius

    def set_radius(self, neo_radius):
        self.radius = neo_radius

    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")

    @classmethod
    def get_num_circles(cls):
        return cls.num_circles


class Rectangle(Shape):
    num_rectangles = 0

    def __init__(self, colors, width, height):
        super().__init__(colors)
        type(self).num_rectangles += 1
        self.width = width
        self.height = height

    def draw(self):
        print("Drawing a rectangle with width {} height {}".format(self.width, self.height))

    def set_width(self, neo_width):
        self.width = neo_width

    def set_height(self, neo_height):
        self.height = neo_height

    def print_area(self):
        print("Rectangle width {} height {} has area as "
              "{}".format(self.width, self.height, self.width * self.height))

    @classmethod
    def get_num_rectangles(cls):
        return cls.num_rectangles


if __name__ == '__main__':
    circles = []
    rectangles = []
    NUM_OBJECTS = 3
    MIN = 10
    MAX = 20
    colors = ["green", "yellow", "blue", "red", "pink"]
    for i in range(NUM_OBJECTS):
        colors = random.choice(colors)
        radius = random.randint(MIN, MAX)
        circles.append(Circle(colors, radius))
        circles[i].draw()
    print(f"Num circles is {Circle.get_num_circles()}")

    for i in range(NUM_OBJECTS):
        colors = random.choice(colors)
        width = random.randint(MIN, MAX)
        height = random.randint(MIN, MAX)
        rectangles.append(Rectangle(colors, width, height))
        rectangles[i].draw()
        rectangles[i].print_area()
    print(f"Num rectangle is {Rectangle.get_num_rectangles()}")
