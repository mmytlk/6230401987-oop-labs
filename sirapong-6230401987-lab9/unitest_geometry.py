from geometry import shape, area
import unittest


class TestMath(unittest.TestCase):
    def test_circle(self):
        circle1 = shape.Circle("blue", 3)
        print(f"Checking the area of the circle with radius {circle1.radius}")
        self.assertEqual(round(area.get_circle_area(circle1.radius), 2), 28.27)

    def test_rectangle(self):
        rect1 = shape.Rectangle("green", 3, 4)
        print(f"Checking the area of the rectangle with width {rect1.width} height {rect1.height}")
        self.assertEqual(round(area.get_rectangle_area(rect1.width, rect1.height), 2), 12)


if __name__ == '__main__':
    unittest.main()
