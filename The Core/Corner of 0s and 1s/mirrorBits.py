def solution(a):
    return int(bin(a).replace('0b','')[::-1],2)
