# iBS takes in an array and a value to search for. If the value is found in the array then iBS will return the index where the found value is. If the value is not found in the array then iBS returns false. Make sure your solution is iterative.

def iBS(arr, num):
    for x in range(len(arr)):
        if arr[x] == num:
            return "The number {} is found at index {}.".format(num, x)
    return False

arr = [-90,-19,0,2,12,29,33,190,320]
print(iBS(arr, 5))
print(iBS(arr, 12))
print(iBS(arr, 0))
print(iBS(arr, 190))