import re

def solution(text):
    f = re.findall('[a-zA-Z0-9]+', text)
    return sorted(list(f), key=len, reverse=True)[0]