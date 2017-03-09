# Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
def printOdd():
    for i in range(1,1001):
        print i
    return

# Create another program that prints all the multiples of 5 from 5 to 1,000,000.
def printMultiples():
    for i in range(5,1000001,5):
          print i
    return

# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
def printSumVals(a):
    sum = 0
    for i in range(0,len(a)):
        sum = sum +  a[i]
    print sum
    return sum

# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
def printAverage(a):
    sum = printSumVals(a)
    print (sum/len(a))
    return

a = [1,2,5,10,155,3]
printOdd()
printMultiples()
printSumVals(a)
printAverage(a)
