import random, statistics

number1 = random.randint(1, 11)
number2 = random.randint(1, 11)
average = (number1+number2) / 2
sd = (statistics.pstdev([number1, number2]))

print("The average of %d and %d is %.1f" %(number1, number2, average))
print("The standard deviation of %d and %d is %.2f" %(number1, number2, sd))
