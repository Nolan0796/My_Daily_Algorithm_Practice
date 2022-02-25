#!/bin/python3

import math
import os
import random
import re
import sys

# Write a program that would print all the odd numbers from 1 to 1000

def printAllOdds(num):
    for x in range(1, num+1, +2):
        print(x)


printAllOdds(1000)