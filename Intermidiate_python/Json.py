import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

person_json = json.dumps(person,indent=4)

print(person_json)

person = json.loads(person_json)
print(person)