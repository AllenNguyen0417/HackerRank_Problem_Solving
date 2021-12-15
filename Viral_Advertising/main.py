#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    likes = 0
    people = 5
    for i in range(0, n):
        people = people//2
        likes += people
        people *= 3
        
    return likes
    

if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)