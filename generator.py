myNums = [1, 2, 3, 4, 5]

# Without generator function
def squareNumbers(numbers):
    squaredNumbers = list()
    for number in numbers:
        squaredNumber = number * number
        squaredNumbers.append(squaredNumber)
    return squaredNumbers

print(squareNumbers(myNums))

# With generator function 
def generateSquareNumber(numbers):
    for number in numbers:
        yield number * number

result = generateSquareNumber(myNums)

for number in result:
    print(number)