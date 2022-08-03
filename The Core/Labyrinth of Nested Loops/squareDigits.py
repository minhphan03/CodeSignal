def solution(a0):
    occurred = []
    occurred.append(a0)
    l = [int(n)**2 for n in str(a0)]
    s = sum(l)
    while s not in occurred:
        occurred.append(s)
        l = [int(n)**2 for n in str(s)]
        s = sum(l)
    return len(occurred) + 1

print(solution(16))