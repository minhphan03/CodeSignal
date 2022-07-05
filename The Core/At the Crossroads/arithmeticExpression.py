def solution(a, b, c):
    return (a + b == c) or (a - b == c) or (a * b == c) or (a / b == c)

def solution(a, b, c):
    return c in (a+b,a-b,a*b,a/b)