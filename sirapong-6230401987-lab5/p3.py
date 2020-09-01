import math

def mult(a, b):
    try:
        hypotenuse = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
        return hypotenuse
    except TypeError:
        return None


print("hypotenuse({}, {}) is {}".format(3.0, 4.0, mult(3, 4)))
print("hypotenuse({}, {}) is {}".format("3", "4", mult("3", "4")))
print("hypotenuse({}, {}) is {}".format(3, "4.0", mult(3, "4.0")))
