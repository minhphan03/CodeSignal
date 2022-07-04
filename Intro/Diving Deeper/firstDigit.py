def solution(inputString):
    for i in inputString:
        try:
            num = int(i)
            return i
        except ValueError:
            continue