def solution(s):
    prevChar = s[0]
    concated = s[0]
    result = []
    out = []
    for i in s[1:]:
        if i == prevChar:
            concated += prevChar
        else:
            result.append(concated)
            concated = i
        prevChar = i
    result.append(concated)
    for w in result:
        if len(w) > 1:
            out.append(str(len(w)) + w[0])
        else:
            out.append(w)
    return "".join(out)

# solution using itertools
from itertools import groupby
def solution(s):
    x = ''
    for k,g in groupby(s):
        y = len((list(g)))
        if y==1:
            x += k
        else:
            x += str(y) + k
    return x

print(solution("aabbbc"))