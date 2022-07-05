def solution(n):
    hr = n // 60
    m =  n % 60
    return total(hr) + total(m)

def total(n):
    result = 0
    while n> 0:
         result += n % 10
         n = n // 10
    return result