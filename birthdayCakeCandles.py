#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    total = 0
    maximum = max(ar)
    for i in range(0,len(ar)):
        if(ar[i] == maximum):
            total += 1
    return total
if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print(str(result) + '\n')

