# Bubble sort
import math

def bubbleSort(arr):
    for x in range(len(arr)-1):
        count = 0
        for i in range(len(arr)-1-x):
            count = 0
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1
        if count == 0:
            return "{} was finished sorting on interation {}.".format(arr, x+1)
    return "{} was finished sorting on interation {}.".format(arr, x+1)

print(bubbleSort([0,-1,3,4]))
print(bubbleSort([9,-1,-20,40,20,-3]))
