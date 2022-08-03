def solution(n):
    ways = 0
    for i in range(1,n//2 + 1):
        result = 0
        while result < n:
            result += i
            i +=1
            if result == n:
                ways +=1
                break
    return ways
