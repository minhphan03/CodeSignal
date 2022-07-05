def solution(divisor, bound):
    for i in range(0, divisor):
        if (bound-i) % divisor == 0:
            return bound-i
