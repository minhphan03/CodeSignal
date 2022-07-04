def solution(address):
    i = len(address) - 1
    while address[i] != "@":
        i-=1
    return address[i+1:]