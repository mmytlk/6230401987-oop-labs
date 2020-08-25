import sys

def divide(dividend, divisor):
    return dividend / divisor

while True:
    while True:
        try:
            dividend = float(input("Please enter the dividend:"))
        except ValueError:
            print("Please enter a valid number")
        else:
            if dividend < 0:
                exit()
            else:
                break
    while True:
        try:    
            divisor = float(input("Please enter the divisor:"))
        except ValueError:
            print("Please enter a valid number")
        else:
            if divisor < 0:
                exit()
            else:
                break      
    try:
        answer = divide(dividend, divisor)
    except ZeroDivisionError:
        print("Cannot perform division by zero")
    else:
        print('The answer is: {}'.format(answer))
 