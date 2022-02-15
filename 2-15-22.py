def compareTriplets(a, b):
    comparisonPoints = [0,0]
    for x in range(3):
        if type(a[x]) != int:
            return "INTEGER_ARRAY a must have all integers"
        if type(a[x]) != int:
            return "INTEGER_ARRAY b must have all integers"
        if a[x] > b[x]:
            comparisonPoints[0] += 1
        elif a[x] < b[x]:
            comparisonPoints[1] += 1
    return comparisonPoints
        
a = [5,6,7]
b = [3,6,10]

c= [17,28,30]
d= [99,16,8]


print(compareTriplets(a,b))
print(compareTriplets(c,d))