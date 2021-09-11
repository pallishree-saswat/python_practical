# handling json files in python
# javascript object notation abbreviated as JSON is a light-weight data
# interchange format
# It encode python objects as JSON strings,and decode JSON strings into python objects
# // just like dictonary in python
# But we cant index it like dictonary using [name] or key
# to do this we have parse or understand this json data in the form of dictonary or json
# for that there is library called json
# import this first
# it has 4 method
# json.load()  -- decode to dict or python object
# json.loads() --- deocde json strings to python object

import json

with open("./data.json", "r") as file:
    print(file.read())

with open("./data.json", "r") as file:
    d = json.load(file)
    print(d["name"])
    print(d["marks"])
    print(d["subjects"][0])
    print(type(d))

with open("./data.json", "r") as file:
    data = file.read()
    print(data)
    d = json.loads(data)
    print(d)


# covert dictonary to json string
# json.dumps() dict to json string

d = {'name': "jatin", 'marks': 70}
print(d["name"])

string = json.dumps(d)
print(string)
print(type(string))


with open("./data2.json", "w") as file:
    json.dump(d, file)
