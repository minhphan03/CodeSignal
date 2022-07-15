# idea from https://github.com/socathie/CodeFights/blob/master/Arcade/LoopTunnel/Lineup.py

def solution(commands):
    direction = 0
    res = 0
    for n in commands:
        if n == 'L':
            direction -= 90
        elif n == 'R':
            direction += 90
        else:
            direction -= 180
        if direction % 180 == 0:
            res += 1
    return res