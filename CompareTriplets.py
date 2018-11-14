def compareTriplets(a, b):
    result = [0, 0]
    for i in range(0, len(a)):
        if a[i] > b[i]:
            result[0] += 1
        if a[i] < b[i]:
            result[1] += 1
    return result

if __name__ == '__main__':
    a = [1, 2, 3]
    b = [3, 2, 1]
    result = compareTriplets(a, b)
    print(' '.join(map(str, result)))