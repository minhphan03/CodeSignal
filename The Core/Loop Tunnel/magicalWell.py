def solution(a, b, n):
    result = 0
    while n > 0:
        result += a*b
        a +=1
        b +=1
        n -= 1
    return result
