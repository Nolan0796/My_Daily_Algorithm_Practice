# Selection Sort algorithm

def selectionSort(arr):
    for x in range(len(arr)-1):
        print(x)
        min = arr[x]
        swapNeeded = False
        for i in range(x+1, len(arr), +1):
            if arr[i] < min:
                swapNeeded = True
                min = arr[i]
                minIndex = i
        if swapNeeded == True:
            arr[x], arr[minIndex] = arr[minIndex], arr[x]
        else:
            print("No swap needed.")
    return arr

print(selectionSort([3345,2,5,1,0,2,4,6,2,44,444,4]))
