def solution(lastNumberOfDays):
    if lastNumberOfDays in [28, 30]:
        return [31]
    elif lastNumberOfDays == 31:
        return [28, 30, 31]