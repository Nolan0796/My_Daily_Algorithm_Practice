# Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that squares each value in the array.  When the program is done x should have values that have been squared (e.g. [1, 25, 100, 4]).  You're not to use any of the pre-built function in Javascript.  You could for example square the value by saying x[i] = x[i] * x[i];

def squareValues(arr, x=0):
    if x == len(arr):
        return arr
    arr[x] = arr[x] * arr[x]
    return squareValues(arr, x+1)


print(squareValues([1,5,10,-2]))
print(squareValues([0,3,1,-33]))
print(squareValues([10,3,44,-20]))