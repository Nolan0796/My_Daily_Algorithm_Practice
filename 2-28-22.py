#!/bin/python3

import math
import os
import random
import re
import sys

# Write a program that would print the sum of all the odd numbers from 1 to 5000

def sumAllOdds(num):
    sum = 0
    for x in range(1, num+1, +2):
        sum += x
    return sum

print(sumAllOdds(5000))
