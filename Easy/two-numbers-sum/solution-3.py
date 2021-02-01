# time complexity: O(n log n)
# space complexity: O(1)

def twoNumberSum(arr, n):
    arr.sort()
    left = 0
    right = len(arr) - 1
    
    while left < right:
        currentSum = arr[left] + arr[right]
        
        if currentSum == n:
            return [arr[left], arr[right]]
        elif currentSum < n:
            left += 1
        elif currentSum > n:
            right -= 1
    
    return []

print(twoNumberSum([3,5,-4,8,11,1,-1,6], 10))