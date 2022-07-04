def solution(inputString):
    if not inputString[0].isdigit():
        return ""
    i = 0
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            i +=1
        else:
            return inputString[:i]
    return inputString