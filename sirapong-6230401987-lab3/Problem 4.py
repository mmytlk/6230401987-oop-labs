n = int(input("Enter a number to find the factorial :"))

user_factorial = n
factorial = 1

while True:
    factorial = n * factorial
    n -= 1
    if n == 1:
        print(f"Factorial of {user_factorial} is {factorial}")
        break
