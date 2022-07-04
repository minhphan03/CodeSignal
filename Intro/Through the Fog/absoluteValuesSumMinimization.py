def solution(a):
    res = []
    for i in a:
        res.append(sum([abs(i-x) for x in a]))
    return a[res.index(min(res))]