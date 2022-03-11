# Write a program that takes an array of numbers and replaces any number that's negative to a string called 'Dojo'. For example if array = [-1, -3, 2] after your program is done array should be ['Dojo', 'Dojo', 2].

def numberToString(arr, x=0):
    if x == len(arr):
        return arr
    if arr[x] < 0:
        arr[x] = "Dojo"
    return numberToString(arr, x+1)

print(numberToString([-1,-3,2]))