#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    # count = 0
    # for i in range(a,b+1):
    #     if math.sqrt(i).is_integer() == True:
    #         count += 1
    # return count

    # Count all intergers between [sqrt(a), sqrt(b)]
    sqrt_a = math.ceil(math.sqrt(a))
    sqrt_b = math.floor(math.sqrt(b))
    count = 0
    for _ in range(sqrt_a,sqrt_b+1):
        count += 1
    return count

if __name__ == '__main__':
    
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        print(str(result) + '\n')
    

# [1,100] = 1,4,9,16,25,36,49,64,81,100)
