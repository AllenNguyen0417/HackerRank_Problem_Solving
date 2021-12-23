#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    answer = [len(arr)]
    while len(arr) > 0:
        res = []
        for i in arr:
            i = i - min(arr)
            if i != 0:
                res.append(i)
        arr = list(filter((min(arr)).__ne__, arr)) 
        answer.append(len(res))
    answer.remove(0)
    return answer
                


if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))
    print('\n')


# a = [5,4,4,2,2,8]
# ans = [len(a)]
# while len(a) > 0:
#     res = []
#     for i in a:
#         i = i - min(a)
#         if i != 0:
#             res.append(i)
#     a = list(filter((min(a)).__ne__, a))        
#     ans.append(len(res))

# ans.remove(0)
# print(ans)


