#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for i in range(0, len(grades)):
        if((grades[i]%5) >=3 and ((grades[i] - grades[i]%5) + 5) >= 40):
            grades[i] = (grades[i] - grades[i]%5) + 5
    return grades
if __name__ == '__main__':
    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))