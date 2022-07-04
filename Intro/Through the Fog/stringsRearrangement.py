import itertools

def solution(inputArray):
    res = list(itertools.permutations(inputArray))
    for l in res:
        for i in range(len(l)-1):
            if not checkDifference(l[i], l[i+1]):
                break
        else:
            return True
    return False
    

def checkDifference(a, b):
    res = sum([1 for x, y in zip(a,b) if x !=y])
    if res == 0 or res > 1:
        return False
    else:
        return True