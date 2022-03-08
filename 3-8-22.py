# Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that prints the maximum number in the array, minimum value in the array as well as the average values in the array. 



def maxMinAvg(arr, x=0, min=None, max=None, sum=0):
    if min == None:
        min = arr[0]
    if max == None:
        max = arr[0]
    if x == len(arr):
        average = float(float(sum)/len(arr))
        return "Minimum is {}, Maximum is {}, Average is {}".format(min, max, average)
    if arr[x] < min:
        min = arr[x]
    if arr[x] > max:
        max = arr[x]
    sum += arr[x]
    return maxMinAvg(arr, x+1, min=min, max=max, sum=sum)

print(maxMinAvg([1,5,10,-2]))
print(maxMinAvg([-1,-55,-10,-2]))

