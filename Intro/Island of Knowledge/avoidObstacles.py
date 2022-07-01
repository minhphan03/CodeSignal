def solution(inputArray):
    i = 2
    while i <= max(inputArray):
        for num in inputArray:
            if num % i == 0:
                break
        else:
            return i    
        i += 1
    if i > max(inputArray):
        return i
