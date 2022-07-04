def solution(n, firstNumber):
    s =  n // 2 + firstNumber
    if s > n:
        s = s - n
    if s == n:
        return 0
    return s
