if __name__ == '__main__':
    arr = [-4,5 , -2, 0, 4]
    result = [0,0,0]
    for i in range(0, len(arr)):
        if(arr[i] > 0):
            result[0] += 1
        elif(arr[i] == 0):
            result[2] += 1
        else:
            result[1] += 1

    for i in range(0, len(result)):
        print(result[i]/len(arr))

