def find_leaders(arr):
    n = len(arr)
    leaders = []
    
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)
    
    return leaders[::-1]

arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", find_leaders(arr))
