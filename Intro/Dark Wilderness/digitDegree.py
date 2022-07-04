def solution(n):
    steps = 0
    while n >= 10:
        steps +=1
        n = sum([int(i) for i in str(n)])
    return steps

print(chr(97))