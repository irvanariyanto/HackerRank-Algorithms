#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    arr = [int(i) for i in str(n) if int(i) != 0]
    result  = []
    for i in range(0, len(arr)):
        if(n % arr[i] == 0):
            result.append(arr[i])
    return len(result)
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(str(result) + '\n')