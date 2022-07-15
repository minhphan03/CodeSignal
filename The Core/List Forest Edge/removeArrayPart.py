def solution(inputArray, l, r):
    for i in range(r-l+1):
        inputArray.pop(l)
    return inputArray
