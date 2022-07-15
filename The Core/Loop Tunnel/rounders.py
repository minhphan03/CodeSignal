# algorithm from https://github.com/team-orca/CodeFights/blob/master/Answers/rounders.java

def solution(n):
    p = 10
    while n > p:
        # extract the digit
        if (n % p) // (p // 10) < 5:
            n = (n // p) * p
        else:
            # add 1
            n = (n // p + 1) * p
        p *= 10
    
    return n