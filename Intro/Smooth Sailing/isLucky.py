def solution(n):
    l = len(str(n))
    if l % 2 != 0:
        return False
    nums = [int(i) for i in str(n)]
    
    return sum(nums[0:int(l/2)]) == sum(nums[int(l/2):]) 

print(solution(123600))