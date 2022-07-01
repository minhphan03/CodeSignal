def solution(inputString):
    oneOdd = False
    if len(inputString) == 1:
        return True
    count = {}
    for c in inputString:
        if c not in count:
            count[c] = 0
        count[c] += 1
    for occurrence in count.values():
        if occurrence % 2 == 1:
            if oneOdd:
                return False
            else:
                oneOdd == True
    return True
