# Daily_Programming_challenge
def sort012(arr):
    left = 0
    mid = 0
    right = len(arr) - 1
    
    while mid <= right:
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[right], arr[mid] = arr[mid], arr[right]
            right -= 1

arr = [2, 0, 2, 1, 1, 0]
sort012(arr)
print(arr)
