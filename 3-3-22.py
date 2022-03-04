# Given an array with multiple values (e.g. [1,3,5,7,20]), write a program that prints the average of the values in the array.  Again you're not to do this by using of any of the pre-built functions in Javascript.  Again iterate through each number in the array and update the 'average' as the program retrieves each number in the array.

def findAverage(arr):
    total = 0
    for x in range(len(arr)):
        total += arr[x]
        average = float(float(total)/(x+1))
        print("The average for when x = {} is {}.".format(x, average))
    return average

arr1 = [1,3,5,7,20]

print(findAverage(arr1))


