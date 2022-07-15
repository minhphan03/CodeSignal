import re

def solution(n):
    return bool(re.match(r'[1-9]+0+[1-9]+0*', str(n)))