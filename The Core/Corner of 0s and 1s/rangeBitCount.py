def solution(a, b):
    result = 0
    for i in range(a, b+1):
        result += bin(i).count('1')
    return result