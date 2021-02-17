# time complexity is O(n), we will iterate through every number
# space complexity is O(d), the depth of each sub array

def productSum(array, multiplier=1):
    sum = 0
    for el in array:
        if type(el) is list:
            sum += productSum(el, multiplier + 1)
        else:
            sum += el
    return sum * multiplier

arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(arr), len(arr))
