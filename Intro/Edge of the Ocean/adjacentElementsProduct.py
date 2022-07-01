def solution(inputArray):
    i = 1
    largest = inputArray[0]*inputArray[1]
    for i in range(2, len(inputArray)):
        x = inputArray[i-1]
        y = inputArray[i]
        if largest < x*y:
            largest = x*y
    return largest

