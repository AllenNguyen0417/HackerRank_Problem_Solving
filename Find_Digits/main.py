#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    count = 0
    for i in str(n):
        if int(i) == 0:
            continue
        else:
            if n % int(i) == 0:
                count += 1
    return count

if __name__ == '__main__':
    
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        print(str(result) + '\n')

