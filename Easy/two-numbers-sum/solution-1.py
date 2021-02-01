# solution 1: Brute Force
# time complexity: O(n^2)
# space complexity: O(1)

def twoNumberSum(arr, n):
    for i in range(len(arr) - 1):
        firstNum = arr[i]
        for j in range(i + 1, len(arr)):
            secondNum = arr[j]
            
            if firstNum + secondNum == n:
                return [firstNum, secondNum]
    
    return []

print(twoNumberSum([3,5,-4,8,11,1,-1,6], 10))
