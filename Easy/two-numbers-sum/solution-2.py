# time complexity: O(n)
# space complexity: O(n)
def twoNumberSum(arr, n):
    hash={}
    for num in arr:
        match = n - num
        if match in hash:
            return [match, num]
        else:
            hash[num] = True

print(twoNumberSum([3,5,-4,8,11,1,-1,6], 10))
