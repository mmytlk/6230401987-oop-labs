import math


class Number:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        cal = self.x + self.y
        return f"{cal}\n{Number.display(self)}"

    def display(self):
        return f"x is {self.x} and y is {self.y}"

    @classmethod
    def display_factors(cls, x):
        if x % 2 == 1:
            return f"Factors of {x} is {math.floor(x / 2)} and {math.ceil(x / 2)}"
        else:
            return f"Factors of {x} is {x / 2} and {x / 2}"

    @staticmethod
    def is_valid_divisor(x):
        if x == 0:
            return f"{x} is not a valid divisor"
        else:
            return f"{x} is a valid divisor"


if __name__ == '__main__':
    print(f"3 + 5 is {Number(3, 5).add()}")
    print(Number.display_factors(6))
    print(Number.display_factors(8))
    print(Number.is_valid_divisor(2))
    print(Number.is_valid_divisor(0))
