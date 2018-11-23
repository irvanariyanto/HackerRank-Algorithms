#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    bil1 = 0
    bil2 = 0
    for i in range(0, len(arr)):
        bil1+=arr[i][i]
        bil2+=arr[i][(len(arr)-1)-i]
    return abs(bil1-bil2)

if __name__ == '__main__':
    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')
