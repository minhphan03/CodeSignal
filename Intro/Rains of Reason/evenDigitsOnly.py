def solution(n):
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            return False
        n = n // 10
    return True