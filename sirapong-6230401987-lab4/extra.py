try:
    user_number = input("Enter the list of numbers (delimited by a comma): ").split(', ')
    userList = user_number
    print(userList)

    user_index = int(input("Enter an index: "))
    print(userList[user_index])

except IndexError:
    print(f"The list has no element at index {user_index}")
