def solution(current, numberOfDigits):
    if len(str(current)) > numberOfDigits:
        return 0
    num = 0
    current -= 1
    while len(str(current)) <= numberOfDigits:
        current +=1
        num +=1
        numberOfDigits -= len(str(current))   
        
    return current