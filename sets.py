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



