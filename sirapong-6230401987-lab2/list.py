weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(weekday)

weekend = ["Saturday", "Sunday"]
print(weekend)

days = weekday + weekend
print(days)

sorted_days = sorted(days)
print(list(sorted_days))

reverse_days = reversed(days)
print(list(reverse_days))

last2days = days[-2], days[-1]
print(last2days)
