month = ("January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December")
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

user_month = input("Enter month: ")
daysmonth_dict = dict(zip(month, days))

print(f"Number of days in {user_month} is {daysmonth_dict[user_month]}")
