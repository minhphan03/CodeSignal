def solution(inputArray):
    length = {}
    for word in inputArray:
        n = len(word)
        if n not in length:
            length[n] = []
        length[n].append(word)
    
    maxLength = max(list(length.keys()))
    return length[maxLength]
