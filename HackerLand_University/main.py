import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
    lst = []
    for i in grades:
        if i > 35:
            if i % 5 >= 3:
                i = i + (5 - (i % 5))       
        lst.append(i)
    return lst


if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    result = '\n'.join(map(str,result))
    print(result)
