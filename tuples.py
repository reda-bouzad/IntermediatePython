## Tuples are ordered, immutable, allows duplicate elements
## Working with tuples can be more effiecent espcially when working with large data

# creating a tuple
myTuple = ("Max", 28, "Boston")
myOtherTuple = "Reda", 22, "Marrakech"
yetAnotherTuple = ("Jhon",)
tooMuchTuple = tuple(["Doe", 23, "London"])
print(myTuple)
print(myOtherTuple)
print(yetAnotherTuple)
print(tooMuchTuple)

# getting an element of a tuple
item = myTuple[0]
print(item)

# looping over a tuple
for i in myOtherTuple:
    print(i)

# check if an element is inside a tuple
if "Marrakech" in myOtherTuple: 
    print("yes")
else:
    print("no")

# length of a tuple
print(len(myTuple))

# count of an element inside a tuple
print(myTuple.count("Max"))

# index of a given element
print(myTuple.index("Boston"))

# converting a tuple to a list
myList = list(myTuple)
print(myList)

# slicing a tuple
numberTuple = (1, 2, 3, 4, 5, 6, 7)
slicedNumberTuple = numberTuple[0:4]
print(type(slicedNumberTuple))
print(slicedNumberTuple)

# reverse a tuple
reversedNumberTuple = numberTuple[::-1]
print(reversedNumberTuple)

# spreading a tuple
name, age, city = myList
print(name)
print(age)
print(city)

i1, *i2, i3 = numberTuple
print(i1)
print(i3)
print(i2)