# resource from https://sites.google.com/site/tranquangtanqt1990/learn-code/codefights/arcade/1-intro/level-12_5
def solution(product):
    if product == 0:
        return 10
    if product == 1:
        return 1
    smallestNum = ''
    for i in range(9,1,-1):
        while product % i == 0:
            smallestNum = str(i) + smallestNum
            product = product // i
    if product > 1:
        return -1
    return int(smallestNum)   
