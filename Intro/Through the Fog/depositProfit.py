def solution(deposit, rate, threshold):
    res = deposit
    year = 0
    while res < threshold:
        year += 1
        res = (1+ rate/100) * res
    return year
