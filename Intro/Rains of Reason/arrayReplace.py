def solution(inputArray, elemToReplace, substitutionElem):
    result = []
    for n in inputArray:
        if n == elemToReplace:
            result.append(substitutionElem)
        else:
            result.append(n)
    return result
