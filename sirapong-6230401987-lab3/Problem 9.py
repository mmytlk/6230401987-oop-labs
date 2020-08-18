while True:
    user_integers = int(input("Enter an integers:"))
    if user_integers % 2 == 0:
        print(user_integers)
    elif user_integers == 99:
        break
