def check_input(msg):
    while True:
        check = str(input(msg))
        try:
            check = int(check)
        except ValueError:
            print("Please enter a number")
        else:
            return check

while True:
    try:
        first_number = check_input("Please enter the first operand: ")
        second_number = check_input("Please enter the second operand: ")
        operator = str(input("Please enter the operator (+,-,*,/): "))

        if operator == "+":
            print(f"Result of {first_number} + {second_number} is "
                f"{first_number + second_number}")
        elif operator == "-":
            print(f"Result of {first_number} - {second_number} is "
                f"{first_number - second_number}")
        elif operator == "*":
            print(f"Result of {first_number} * {second_number} is "
                f"{first_number * second_number}")
        elif operator == "/":
            print(f"Result of {first_number} / {second_number} is "
                f"{first_number / second_number}")
        else:
            print("Unknown operator")

    except ZeroDivisionError:
        print("Cannot divide by zero")
    exit()
