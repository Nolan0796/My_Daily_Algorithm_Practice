# Write a function to represent a Triangle, given input is the number of rows of the triangle
# Example - if the number of rows are 3
# Result:-
# 1
# 2 3
# 4 5 6

def Triangle(rows):
    row = "1"
    for x in range(1, rows+1):
        print(row)
        if x > 3 and x <14:
            row = str(int(row[len(row)-3] + row[len(row)-2]) + 1) + " "
        elif x > 13:
            row = str(int(row[len(row)-4] + row[len(row)-3] + row[len(row)-2]) + 1) + " "
        else:
            row = str(int(row[len(row)-2])+1) + " "
        for y in range(1, x+1):
            if x < 4:
                row += str(int(row[0])+1*y) + " "
            elif x > 3 and x < 13:
                row += str(int(row[0] + row[1]) + (1*y)) + " "
            else:
                row += str(int(row[0] + row[1] + row[2]) + (1*y)) + " "
Triangle(3)
Triangle(15)
