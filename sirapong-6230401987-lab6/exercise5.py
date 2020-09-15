import json

hobbies =\
    {
    "firstName": "Jane", "lastName": "Doe",
     "hobbies": ["running", "sky diving", "singing"]
    }

with open('hobbies.json', 'w') as f:
    json.dump(hobbies, f)
    
with open('hobbies.json', 'r') as i:
    print(json.load(i))
