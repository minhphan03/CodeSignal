import re

def solution(inputString):
    mat = re.match(r'^\w{2}-\w{2}-\w{2}-\w{2}-\w{2}-\w{2}$', inputString)
    if bool(mat) == False:
        return False
    for i in inputString.split('-'):
        for c in i: 
            if not (48 <= ord(c) <= 57) and not (65 <= ord(c) <= 70):
                return False
    return True

def solution(s):
    return bool(re.match(('^' + '[\dA-F]{2}-' * 6)[:-1] + '$', s)) # [-1] to remove the last hyphen

print(solution('00-1B-63-84-45-E6'))