# # a = [1,7,2,4]
# a = [19,10,12,10,24,25,22]
# k = 4
# s = []


# for i in range(0,len(a),1):
#     for j in range(i+1,len(a),1):
#         if (a[i] + a[j]) %k != 0:
#             s.append([a[i],a[j]])
# print(s)

# # for i in range(0,len(a),1):
# #     for j in range(i+1,len(a),1):
# #         if (a[i] + a[j]) %k != 0:
# #             s.append([a[i],a[j]])
# # print(s)
# # for i in range(0, len(s), 1):
# #     # print(s[i])
# #     for j in range(0, len(a), 1):
# #         if a[j] not in s[i] and (sum(s[i]) + a[j]) %k != 0:
# #             s[i].append(a[j])

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    counts = [0] * k
    for i in s:
        counts[i % k] += 1
    count = min(counts[0], 1)
    for i in range(1, k//2 + 1):
        if i != k-i:
            count += max(counts[i],counts[k-i])
    if k % 2 ==0:
        count += 1
    return count

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(str(result) + '\n')

    
