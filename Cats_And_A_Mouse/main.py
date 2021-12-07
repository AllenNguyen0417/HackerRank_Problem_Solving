#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    A_C = abs(z-x)
    B_C = abs(z-y)
    if A_C < B_C:
        return 'Cat A'
    elif A_C == B_C:
        return 'Mouse C'
    else:
        return 'Cat B'

if __name__ == '__main__':
    

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

    print(result)

        
