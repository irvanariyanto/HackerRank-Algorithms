#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minimum = 0
    maximum = 0
    for i in range(0, len(arr)):
        if(min(arr) != max(arr)):
            if(arr[i] != max(arr)):
                minimum += arr[i]
            if (arr[i] != min(arr)):
                maximum += arr[i]
        else:
            minimum = 4*arr[i]
            maximum = 4*arr[i]
    print (minimum, maximum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
