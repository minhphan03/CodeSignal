def solution(a):
    b = ''
    for n in a:
        b = format(n,'#010b').replace("0b", "") + b
    return int(b, 2)

print(solution([24, 85, 0]))