def solution(upSpeed, downSpeed, desiredHeight):
    height = upSpeed
    day = 1
    while height < desiredHeight:
        height += upSpeed - downSpeed
        day +=1
    return day