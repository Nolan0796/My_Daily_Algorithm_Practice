# Given an array x (e.g. [1,5, 10, 7, -2]), create an algorithm (sets of instructions) that shifts each number by one (to the front).  For example when the program is done x (assuming it was [1,5,10,7,-2]) should become [5,10,7,-2, 0].  

def shiftingArrValues(arr, x=0):
    if x == len(arr)-1:
        arr[x] = 0
        return arr
    arr[x] = arr[x+1]
    return shiftingArrValues(arr, x+1)

print(shiftingArrValues([1, 5, 10, 7, -2]))