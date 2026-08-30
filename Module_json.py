import json


#   CONVERTING JSON FILE DATA INTO THE DICTIONARY
with open("gg.json","r") as a:
    gg=json.load(a)

print(gg)

# CONVERTING json string into dictinary
data = '{"name": "Shubham", "age": 19, "city": "Jaipur", "is_student": true}'

a=json.loads(data)
print(a)

#   CONVERTING python dictinary string DATA INTO THE JSON
import json

data = {
    "name": "Shubham",
    "age": 19,
    "city": "Jaipur",
    "is_student": True
}

result = json.dumps(data)

print(result)
print(type(result))

#CONVERTING JSON FILE DATA INTO THE DICTIONARY
import json

data = {
    "name": "Shubham",
    "age": 19,
    "city": "Jaipur",
    "is_student": True
}

with open("data.json", "w") as file:
    json.dump(data, file)


data={"Name":"Shubham","City":"Jaipur","Roll":70,"Age":80}

a=json.dumps(data)

print(a)