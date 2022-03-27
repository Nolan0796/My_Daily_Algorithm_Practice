# Write a function rFibonacci using recursion

def rFibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return rFibonacci(num-1) + rFibonacci(num-2)
    
print(rFibonacci(0))
print(rFibonacci(1))
print(rFibonacci(2))
print(rFibonacci(3))
print(rFibonacci(4))
print(rFibonacci(5))