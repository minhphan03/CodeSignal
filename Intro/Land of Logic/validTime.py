def solution(time):
    e = time.split(':')
    if 0<= int(e[0]) <= 23 and 0 <= int(e[1]) <= 59:
        return True
    return False