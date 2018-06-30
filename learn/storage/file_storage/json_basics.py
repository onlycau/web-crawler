import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data=json.loads(str)
print(data)
print(type(data))
print(data[0]['name'],data[0].get('name'))

#Call the 'dumps()' method to convert Json objects to strings.
with open('data.json','w') as file:
    file.write(json.dumps(data,indent=2))