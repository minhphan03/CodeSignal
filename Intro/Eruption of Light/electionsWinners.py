# exceed runtime in one of the tests
def solution(votes, k):
    res = 0
    for i in range(len(votes)):
        c = votes.pop(i)
        if c+k > max(votes):
            res += 1
        votes.insert(i, c)
    return res

def solution(votes, k):
    if k == 0:
        votes.sort(reverse = True)
        if votes.count(votes[0]) == 1:
            return 1
        else:
            return 0
    else:
        result = 0
        votes.sort(reverse = True)
        max_ = votes[0]
        for i in votes:
            if i+k > max_:
                result +=1
        return result