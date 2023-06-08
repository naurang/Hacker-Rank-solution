#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    total = 0
    n = len(s)                   # n = 5, d = 3, m = 2, [1,2,1,3,2]
    for i in range((n - m) + 1): # Ex.(5-2)+1 = 4
        if sum(s[i:i+m]) == d:    # sum[0:2], (1+2) = 3 , sum[1:3], (2+1) = 3 
            total += 1
    return total
             
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
