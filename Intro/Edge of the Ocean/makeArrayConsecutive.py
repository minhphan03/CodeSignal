def solution(statues):
    statues = sorted(statues)
    return statues[-1] - statues[0] - len(statues) + 1
