# Sets: unordered, mutable, no duplicates

mySet = {"red", "blue", "green"}
mySet.add("pink")
mySet.add("yellow")
mySet.remove("red")
mySet.discard("purplani")
print(mySet.pop())
print(mySet)

# looping through a set
for i in mySet:
    print(i)

# checking if an item is a set
if "yellow" in mySet:
    print("yes")
else:
    print("no")

# sets dont allow duplication
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

y = odds.intersection(primes)
print(y)

w = evens.intersection(primes)
print(w)

setA = {1, 3, 4, 6, 8, 11}
setB = {1, 2, 3, 7, 5, 10}

diffA = setA.difference(setB)
diffB = setB.difference(setA)
symDiff = setA.symmetric_difference(setB)
mySymDiff = diffA.union(diffB)
print(diffA)
print(diffB)
print(mySymDiff)
print(symDiff)

# updating a set
championsList = {"Jhon", "Adam", "Rob"}
heroesList = {"Bob", "Jhon", "Linda"}
championsList.update(heroesList)


# intersection
colorsList = {"red", "blue", "green"}
anotherColorsList = {"pink", "blue", "yellow"}

colorsList.intersection_update(anotherColorsList)
print(colorsList)

# subsets
setUp = {1, 2, 3, 4, 5, 6}
setDown = {1, 2, 3}

print(setUp.issubset(setDown))
print(setDown.issubset(setUp))


# forozen set
myFrozenSet = frozenset({"Max", "Darc", "Jhon"})
print(myFrozenSet)

