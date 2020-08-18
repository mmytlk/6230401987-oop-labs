n = int(input("Enter a number to find the factorial : "))

user_factorial = n
factorial = 1
fac01 = 1

while True:
    factorial = n * factorial
    n -= 1
    if user_factorial == 1 or user_factorial == 0 :
        print(f"Factorial of {user_factorial} is {fac01}")
        break
    elif n == 1:
        print(f"Factorial of {user_factorial} is {factorial}")
        break
