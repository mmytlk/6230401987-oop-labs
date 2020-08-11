contacts_dict =	{"Jane Doe" : "+27 555 5367",
  "John Smith" : "+27 555 6254",
  "Bob Stone" : "+27 555 5689"}
  
contacts_dict["Jane Doe"] = "+27 555 1024"
contacts_dict["Anna Cooper"] = "+27 555 3237"

print(contacts_dict.get("Bob Stone"))

if "Bob Stone" in contacts_dict:
    print(contacts_dict.get("Bob Stone"))
else:
    pass

contacts_keys = list(contacts_dict.keys())
contacts_values = list(contacts_dict.values())

print(contacts_keys)
print(contacts_values)
