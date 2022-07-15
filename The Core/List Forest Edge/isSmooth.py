def solution(arr):
    if len(arr) % 2 == 1:
        return arr[0] == arr[-1] and arr[0] == arr[(len(arr)//2)]
    else:
        return arr[0] == arr[-1] and arr[0] == (arr[len(arr)//2] + arr[len(arr)//2 - 1])
