## Lists are ordered, mutable, allows duplicate elements ##

# creating a new list:
myList = ['Apple', 'Banana', True, 5]
numberList = [15, 2, 14, 13]
print(myList)

# creating an empty list:
myOtherList = list();
print(myOtherList) 


# looping through a list:
for i in myList:
    print(i) 

# checking if an item is inside a list:
if "Apple" in myList:
    print("yes")
else:
    print("no")

# lenght of an array:
print(len(myList))

# appending an element to the end of an array
myList.append("blue")
print(myList)

# inserting an element in a given index
myList.insert(0, "red")
print(myList)

# remove the last item of an array
myList.pop()
print(myList)

# removing an elment based on its value
myList.remove("red")
print(myList)

# reverse an array
myList.reverse()
print(myList)

# sorting a list (changes the original array)
print(numberList)
numberList.sort()
print(numberList)

# sorting a list (without changing the original array)
numberList.append(-5)
print(numberList)
new_number_list = sorted(numberList)
print(new_number_list)
print(numberList)

# duplicationg an element
earthList = [0] * 5
print(earthList)

# concatenateList
moonList = [4] * 5
print(moonList)
sunList = earthList + moonList
print(sunList)

# slicing a list
jupiterList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
venusList = jupiterList[2:4]
plutoList = jupiterList[:4]
erisList = jupiterList[::2]
print(venusList)
print(plutoList)
print(erisList)

# copying a list : when we modify blueList we also modify redList, they refere to the same list in the memory
redList = ["planet", "galaxy", "star"]
blueList = redList
blueList.append("sun")
print(redList)
print(blueList)

# cloning a list 
yellowList = ["tea", "cafe", "juice"]
greenList = yellowList.copy()
yellowList.append("water")
print(yellowList)
print(greenList)

# changing everyElement in array
blackList = [1, 2, 3, 4, 5]
whiteList = [i*i for i in blackList]
print(whiteList)

# removing all elements on array
myList.clear()
print(myList)