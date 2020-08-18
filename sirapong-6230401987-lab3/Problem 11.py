while True:
    try:
        first_number = float(input("Enter the first number: "))
        if first_number == "quit":
            break
        second_number = float(input("Enter the second number: "))
        if second_number == "quit":
            break
        operator = str(input("Enter the operator: "))
    except ValueError:
        break
    if operator == "+":
        print(f"{first_number} + {second_number} = "
              f"{first_number + second_number}")
    elif operator == "-":
        print(f"{first_number} - {second_number} = "
              f"{first_number - second_number}")
    elif operator == "*":
        print(f"{first_number} * {second_number} = "
              f"{first_number * second_number}")
    elif operator == "/":
        if first_number == 0 or second_number == 0:
            print("Cannot divide a number by 0")
        else:
            print(f"{first_number} / {second_number} = "
                  f"{first_number / second_number}")
    elif operator == "quit":
        break
    else:
        print("Unknown operator")
