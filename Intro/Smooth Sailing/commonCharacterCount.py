def solution(s1, s2):
    dict1 = build_dict(s1)
    dict2 = build_dict(s2)
    total = 0
    for k in dict1.keys():
        if k in dict2:
            total += min(dict1[k], dict2[k])
    return total

def build_dict(s):
    result = {}
    for c in s:
        if c not in result:
            result[c] = 1
        else:
            result[c] +=1
    return result
