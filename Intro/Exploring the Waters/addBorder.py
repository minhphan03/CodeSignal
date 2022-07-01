def solution(picture):
    height = len(picture)
    width = len(picture[0])
    
    result = []
    result.append('*'*(width+2))
    for line in picture:
        result.append('*' + line + "*")
    result.append('*'*(width+2))
    return result
