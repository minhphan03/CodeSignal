def solution(n, l, r):
    i = l
    result = 0
    used = []
    while i <= r:
        if l <= (n-i) <= r and i not in used:
            result += 1
            used.append(n-i)
        i +=1
    return result 