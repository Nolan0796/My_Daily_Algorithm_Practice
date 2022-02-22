#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for x in range(len(grades)):
        if grades[x] < 38:
            continue
        if (grades[x] + 1) % 5 == 0:
            grades[x] += 1
            continue
        if (grades[x] + 2) % 5 == 0:
            grades[x] += 2
            continue
    return grades

grade_list = [73,67,38,33]
grade_list1 = [20,51,87,90]

print(gradingStudents(grade_list))
print(gradingStudents(grade_list1))