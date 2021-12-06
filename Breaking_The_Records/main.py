#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    max = scores[0]
    min = scores[0]
    count_best = 0
    count_worst = 0

    for i in scores:
        if i > max:
            count_best += 1
            max = i
        elif i < min:
            count_worst += 1
            min = i

    return count_best, count_worst

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
