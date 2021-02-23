def hourglassSum(arr):
    maxval = None
    for j in range(4):
        for i in range(4):
            add = arr[j][i] + arr[j][i+1] + arr[j][i+2] + arr[j+1][i+1] + arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2]
            print(j,i, 'the sum is', add)
            if maxval == None:
                maxval = add
            elif add > maxval:
                maxval = add
    return maxval

arr = [
    [1, 1, 1, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0], 
    [0, 0, 0, 2, 0, 0], 
    [0, 0, 1, 2, 4, 0]
]

print(hourglassSum(arr))
