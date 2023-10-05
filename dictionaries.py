## Dictionary: key-value pairs, Unoreded, Mutable


# creating a dictionary
myDict = {"name": "Max", "age":28, "city": "New York"}
print(myDict)
anotherDict = dict(name="Mary", age="33", city="Boston")
print(anotherDict)


# getting an element inside of dictionary
print(myDict["name"])


# adding a key-value inside of a dictionary
myDict["email"] = "max@gmail.com"
print(myDict)


# changing a value inside of a dictionary
myDict["name"] =  "Reda"
print(myDict)


# deleting a key-value pair inside of a dictionary
del myDict["name"]
print(myDict)
myDict.pop("age")
print(myDict)


# checking if an item is inside a dictionary
if "city" in myDict:
    print(myDict["city"])

try:
    print(myDict["name"])
except:
    print("name does not exist")

# looping through keys inside a dictionnary
for key in myDict.keys():
    print(key)


# looping through valuess inside a dictionnary
for value in myDict.values():
    print(value)


# updating a dictionary
clientDetail = {"firstName": "Reda", "lastName": "Bouzad", "age": 22, "city": "Marrakech"}
newClientDetail = {"firstName": "Reda", "age": 30, "city": "Boston"}

print(clientDetail)
clientDetail.update(newClientDetail)
print(clientDetail)

