def solution(a):
    team1 = 0
    team2 = 0
    u = len(a)
    i = 1
    while i < u:
        team1 += a[i-1]
        team2 += a[i]
        i +=2
    if i == u:
        team1 += a[i-1]
    return [team1, team2]
