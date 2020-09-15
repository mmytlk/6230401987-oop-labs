import json

with open('hobbies.json', 'r') as f:
    data = json.load(f)
    seperate = ", "
    print(data['firstName']+ " has hobbies as " + seperate.join(data['hobbies']))
