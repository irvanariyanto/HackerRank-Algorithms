#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    arr=s.split(":")
    if(arr[2][-2:] == "PM"):
        if(int(arr[0]) >= 12):
            arr[2] = arr[2].replace("PM","")
        else:
            arr[2] = arr[2].replace("PM", "")
            arr[0] = str(int(arr[0])+12)
    else:
        if (int(arr[0]) < 12):
            arr[2] = arr[2].replace("AM", "")
        else:
            arr[2] = arr[2].replace("AM", "")
            arr[0] = str(int(arr[0]) - 12)
    for i in range(0, len(arr)):
        if(int(arr[i]) < 10 and len(arr[i]) < 2):
            arr[i]= "0"+arr[i]
    return ":".join(arr)

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)