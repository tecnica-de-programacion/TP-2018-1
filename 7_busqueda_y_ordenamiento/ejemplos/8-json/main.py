import json

new_person = {
    "_id": "59a8d1510042e4ac60c97ce4",
    "isActive": False,
    "age": 34,
    "name": "Miguel Simpson"
}

# Read People
try:
    people_file = open('people.json', 'r+')
    people = json.load(people_file)
except FileNotFoundError:
    print('Error W testfile')
else:
    for person in people:
        print('---' * 5)
        for key, value in person.items():
            print("{:9}: {}".format(key, value))
finally:
    people_file.close()



try:
    people_file = open('people.json', 'w')
except FileNotFoundError:
    print('Error W testfile')
else:
    people.append(new_person)
    people_json_format = json.dumps(people, indent=2)
    people_file.seek(0, 0)
    people_file.write(people_json_format)
finally:
    people_file.close()