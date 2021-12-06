#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below
#
def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    lst = []
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i]+drives[j] <= b:
                lst.append(sum([keyboards[i],drives[j]]))
    if len(lst) == 0:
        return -1
    else:
        lst.sort()
        return lst
    
        

if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
