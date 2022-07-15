def solution(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp
    return arr
