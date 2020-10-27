import mathz
import unittest


class TestMath(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(mathz.sums(1, 2), 3)
        self.assertEqual(mathz.sums(1.1, 2.3), 3.4)

    def test_subtract(self):
        self.assertEqual(mathz.subtract(10, 2), 8)
        self.assertEqual(mathz.subtract(-3, 2), -5)

    def test_mul(self):
        self.assertEqual(mathz.mul(2, 3), 6)
        self.assertEqual(mathz.mul(-1, -2), 2)

    def test_divide(self):
        self.assertEqual(mathz.divide(10, 2), 5)
        self.assertEqual(mathz.divide(3, 2), 1.5)
        self.assertRaises(ValueError, mathz.divide, 12, 0)


if __name__ == '__main__':
    unittest.main()
