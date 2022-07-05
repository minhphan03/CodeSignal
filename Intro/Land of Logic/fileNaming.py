def solution(names):
    result = []
    for i in names:
        if i not in result:
            result.append(i)
        else:
            k = 1
            while i + "(" + str(k) + ")" in result:
                k +=1
            else:
                result.append(i + "(" + str(k) + ")")
    return result 
