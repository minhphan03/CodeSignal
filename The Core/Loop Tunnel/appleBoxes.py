def solution(k):
    odds = sum([n*n for n in range(k+1) if n % 2 == 1])
    evens = sum([n*n for n in range(k+1) if n % 2 == 0])
    return evens - odds
    
print(solution(5))