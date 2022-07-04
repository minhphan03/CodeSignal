def solution(inputArray, k):
    res = []
    for i in range(len(inputArray)):
        if (i+1)%k != 0:
            res.append(inputArray[i])
    return res
