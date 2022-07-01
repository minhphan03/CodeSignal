def solution(a, b):
    count = 0
    diff1 = []
    diff2 = []
    for n1, n2 in zip(a, b):
        if n1 != n2:
            count +=1
            diff1.append(n1)
            diff2.append(n2)
    if count == 0 or count == 2:
        if set(diff1) == set(diff2):
            return True
    return False