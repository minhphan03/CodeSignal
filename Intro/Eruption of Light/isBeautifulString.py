from collections import OrderedDict,  OrderedDict

def solution(inputString):
    d = {}
    for i in range(97, 123):
        d[chr(i)] = 0
    for c in inputString:
        d[c] += 1
    od = OrderedDict(sorted(d.items()))
    if list(od.values()) != sorted(list(od.values()), reverse=True):
        return False
    return True
