month = ("January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December")
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
dict_items = {}

for i in range(0, 12):
    dict_items[month[i]] = days[i]

user_month = input("Enter month: ")
print(f"Number of days in {user_month} is {dict_items[user_month]}")
