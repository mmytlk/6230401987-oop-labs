import datetime

name = str(input("Enter your name:"))
year = int(input("Enter your year you were born:"))
now = datetime.datetime.now()
thisyear = now.year
age = thisyear - year

if age >= 1 and age <= 9:
    print("%s is %d years old. You are generation \"Alpha\"" % (name, age))
if age >= 10 and age <= 24:
    print("%s is %d years old. You are generation \"Z\"" % (name, age))
if age >= 25 and age <= 39:
    print("%s is %d years old. You are generation \"Y\"" % (name, age))
if age >= 40 and age <= 54:
    print("%s is %d years old. You are generation \"X\"" % (name, age))
if age >= 55 and age <= 72:
    print("%s is %d years old. You are generation \"Baby Boomer\"" % (name, age))
if age >= 73:
    print("%s is %d years old. You are generation \"Builder\"" % (name, age))