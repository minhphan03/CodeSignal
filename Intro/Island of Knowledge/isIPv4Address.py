import re

def solution(inputString):
    if bool(re.match(r'^\d+\.\d+\.\d+\.\d+$', inputString)) == False:
        return False
    for i in inputString.split("."):
        if i != str(int(i)):
            return False
        if int(i) > 255 or int(i) < 0:
            return False
    return True
