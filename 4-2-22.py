# Insertion Sort

def insertionSort(arr):
    for x in range(1, len(arr), +1):
        valueToCompare = arr[x]
        i = x
        while i > 0 and arr[i-1] > valueToCompare:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = valueToCompare
    return arr

print(insertionSort([2,3,1,0]))

