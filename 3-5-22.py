# Write a program that takes an array and returns the number of values in that array whose value is greater than y. For example, if array = [1,3, 5, 7] and y = 3, after your program is run it will print 2 (since there are two values in the array whose value is greater than 3).  Again make sure you come up with a simple base case and write instructions to solve that base case first and then test your instructions for other complicated cases. You can use a count function with this assignment.

def greaterThanY(arr, y, num=0, count=0):
    if num == len(arr):
        return count
    if arr[num] > y:
        count +=1
    return greaterThanY(arr, y, num+1, count = count)

arr1 = [1,3, 5, 7]
arr2 = [30,4,33,87,.5,90]
print(greaterThanY(arr1, 3))
print(greaterThanY(arr2, 31))