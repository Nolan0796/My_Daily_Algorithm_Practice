# Write a function rFactorial

def rFactorial(num, x=1, product=1):
    if x > num:
        return product
    else:
        product = product*x
    return rFactorial(num, x+1, product=product)

print(rFactorial(3))
print(rFactorial(4))
print(rFactorial(8))
