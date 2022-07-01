def solution(inputArray):
    moves = 0
    l = len(inputArray)
    i = 0
    while i < len(inputArray)-1:
        if inputArray[i+1] <= inputArray[i]:
            moves += inputArray[i]+1-inputArray[i+1]
            inputArray[i+1] = inputArray[i] + 1
        i +=1
    return moves