def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    if weight2 > maxW and weight1 > maxW:
        return 0
    if weight1 > maxW:
        return value2
    if weight2 > maxW:
        return value1
    else:
        return max(value1, value2)

# solution 2
def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        return max(value1 if weight1 <= maxW else 0, value2 if weight2 <= maxW else 0)