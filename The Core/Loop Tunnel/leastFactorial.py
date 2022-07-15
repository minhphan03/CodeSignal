def solution(n):
    result = 1
    i = 1
    while result < n:
        result *= i
        i +=1
    return result
