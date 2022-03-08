# Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that replaces any negative number with the value of 0.  When the program is done x should have no negative values (e.g. [1, 5, 10, 0]).

def elminateNegativeNumbers(arr):
    for x in range(len(arr)):
        if arr[x] < 0:
            arr[x] = 0
    return arr

print(elminateNegativeNumbers([1, 5, 10, -2]))