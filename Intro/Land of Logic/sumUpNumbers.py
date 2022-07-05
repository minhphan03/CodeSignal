import re
def solution(inputString):
    f = re.findall('\d+', inputString)
    return sum([int(n) for n in list(f)])