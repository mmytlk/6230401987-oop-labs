def robust_calculator():
    while True:
        first_num = input_op("Please enter the first operand ('q' to quit):" )
        second_num = input_op("Please enter the second operand: ")
        operator = cal_op()
        if operator is None:
            continue
        format_re = format()
        output = cal(first_num, second_num, operator, format_re)
        if output is not None:
            print("{} {} {} = {}".format(first_num, operator, second_num, output))
        else:
            print("We cannot perform your request calculation")


def input_op(msg):
    while True:
        a = input(msg)
        try:
            if a.lower() == "q":
                exit()
            else:
                a = float(a)
                return a
        except ValueError:
            print("Please enter the operand or q.")
        continue


def cal_op():
    cal_num = input("Enter an operation ('+', '-', '*', '/'): ")
    if cal_num == "(":
        print("Operation must be ADD, SUB, MUL, or DIV")
        return None
    elif cal_num == "":
        cal_num = "+"
    return cal_num


def format():
    format_value = input("Enter output format (float, int): ")
    if format_value == "":
        format_value = "float"
    return format_value


def cal(first_num, second_num, cal_num, format_re):
    if cal_num == "+":
        result = first_num + second_num
    elif cal_num == "-":
        result = first_num - second_num
    elif cal_num == "*":
        result = first_num * second_num
    elif cal_num == "/":
        try:
            result = first_num / second_num
        except ZeroDivisionError:
            print("Cannot divide by 0")
            return None
    else:
        return None
    if format_re == "float":
        result = float(result)
    elif format_re == "int":
        result = int(round(result))
    else:
        return None
    return result


if __name__ == '__main__':
    robust_calculator()
