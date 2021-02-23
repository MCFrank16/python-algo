from collections import deque

def rotateLeft(d, arr):
    items = deque(arr)
    while d > 0:
        item = items.popleft()
        items.append(item)
        d -= 1
    
    return list(items)

arr = [1,2,3,4,5]
d = 2

print(rotateLeft(d,arr))