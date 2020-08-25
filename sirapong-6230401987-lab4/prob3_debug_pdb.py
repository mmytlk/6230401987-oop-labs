import sys, pdb

def divide(dividend, divisor):
    return dividend / divisor

while True:
    dividend = input("Please enter the dividend:")
    divisor = input("Please enter the divisor:")
    pdb.set_trace()
    if dividend < 0 or divisor < 0:
	    break
    answer = divide(dividend, divisor)
    print('The answer is: {}'.format(answer))
 