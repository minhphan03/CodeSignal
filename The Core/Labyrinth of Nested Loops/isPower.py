def solution(n):
    if n == 1:
        return True 
    for i in range(2, n//2 + 1):
        t = n
        while t % i == 0:
            t = t // i
            if t == 1:
                return True
    return False