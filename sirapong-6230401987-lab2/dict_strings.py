pairs = {"manee": '1234', "mana": '4567', "chujai": '6789'}
pairs_set = set(pairs.items())

list_pairs = list(pairs_set)
print(list_pairs)
list_values = list(pairs.values())
print(list_values)
list_key = list(pairs.keys())
print(list_key)

word = list("antidisestablishmentarianism")
word.sort()
join_word = "".join(word)
print(join_word)

print("the|quick|brown|fox|jumped|over|the|lazy|dog".split("|"))
