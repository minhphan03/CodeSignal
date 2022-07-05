# approach by GeeksbyGeeks
# https://www.geeksforgeeks.org/largest-number-possible-after-removal-of-k-digits/ 

def solution(n):
    ans = 0
    i = 1
    while n // i > 0:
        # whole-divide more than necessary (10*i) to remove the middle digit
        res = (n//(10*i))*i + n % i
        ans = max(ans, res)
        i *=10
    return ans