def solution(inputArray):
    maxAbs = 0
    i = 0
    while i < len(inputArray) -1:
        if abs(inputArray[i] - inputArray[i+1]) > maxAbs:
            maxAbs = abs(inputArray[i] - inputArray[i+1])
        i +=1
    return maxAbs
