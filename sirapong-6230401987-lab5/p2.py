import math

def hypotenuse(a, b):
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    print("Sqrt({}^2 + {}^2) = {}".format(a ,b ,c))


hypotenuse(3.0, 4.0)
hypotenuse(3, 4)
hypotenuse(3, 4.0)
