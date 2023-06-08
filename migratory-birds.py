#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    zero, one, two, three, four, five = 0,0,0,0,0,0
    for i in arr:
        if i == 1:
           one += 1 
        elif i == 2:
            two += 1
        elif i == 3:
            three +=1
        elif i == 4:
            four += 1
        elif i == 5:
            five += 1
        else:
            zero += 1  
    tp = [zero, one, two, three, four, five]
    return tp.index(max(tp))  
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
