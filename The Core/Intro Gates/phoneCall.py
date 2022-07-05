def solution(min1, min2_10, min11, s):
    total = 0
    if s >= min1:
        s -= min1
        total +=1
    else:
        return total
    if s >= 9*min2_10:
        s -= 9*min2_10
        total += 9
    else:
        total += s // min2_10
        return total
    return total + s // min11
        
