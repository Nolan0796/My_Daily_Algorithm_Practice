# Find the 2nd largest and 2nd smallest number in two arrays of numbers combined
# Example:- [10,5,7,2,4,1,24] & [8,23,29,25,40,0,24] Result:-2nd Largest: 29 && 2nd Smallest: 1

def secondLargestSmallest(arr):
    min = arr[0]
    secondMin = arr[0]
    max = arr[0]
    secondMax = arr[0]
    for x in range(len(arr)):
        if arr[x] < secondMin:
            if arr[x] < min:
                secondMin = min
                min = arr[x]
            else:
                secondMin = arr[x]
        if arr[x] > secondMax:
            if arr[x] > max:
                secondMax = max
                max = arr[x]
            else:
                secondMax = arr[x]
    return "Second smallest = {}, Second largest = {}".format(secondMin, secondMax)

print(secondLargestSmallest([10,5,7,2,4,1,24]))