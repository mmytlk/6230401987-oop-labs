check_input = False

while not check_input:
    try:
        temp_f = float(input("Enter a temperature in Farenheit: "))
        temp_c = (5 / 9) * (temp_f - 32)
        print("Temperature %.2f in Farenheit is %.2f in Celsius"
              % (temp_f, temp_c))
    except ValueError:
        print("Please enter a valid floating point for the temperature.")
    else:
        check_input = True
