def solution(param1, param2):
    if param1 > param2:
        i = len(str(param1))
        param2 = format(param2, '0{}d'.format(i))
        param1 = str(param1)
    else:
        i = len(str(param2))
        param1 = format(param1, '0{}d'.format(i))
        param2 = str(param2)
    return int(''.join([str((int(x) + int(y))%10) for x, y in zip(param1, param2)]))

print(int(solution(456, 1734)))