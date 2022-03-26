# Write a function iFibonacci

def iFibonacci(num):
    series = []
    for x in range(num+1):
        if x == 0:
            series.append(x)
        elif x ==1:
            series.append(x)
        else:
            nextNum = 0
            firstNum = series[x-1]
            nextNum += firstNum
            secondNum = series[x-2]
            nextNum += secondNum
            series.append(nextNum)
    return series[len(series)-1]

print(iFibonacci(0))
print(iFibonacci(1))
print(iFibonacci(2))
print(iFibonacci(3))
print(iFibonacci(5))