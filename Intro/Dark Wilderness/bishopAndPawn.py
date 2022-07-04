def solution(bishop, pawn):
    moves = set()
    # ord(a) = 97, ord(h) = 104
    f = ord(bishop[0])
    l = int(bishop[1])
    while f <= 104 and l <= 8:
        moves.add(chr(f) + "" + str(l))
        f +=1
        l +=1
    f = ord(bishop[0])
    l = int(bishop[1])
    while f <= 104 and l >= 1:
        moves.add(chr(f) + "" + str(l))
        f +=1
        l -=1
    f = ord(bishop[0])
    l = int(bishop[1])
    while f >= 97 and l >= 1:
        moves.add(chr(f) + "" + str(l))
        f -=1
        l -=1
    f = ord(bishop[0])
    l = int(bishop[1])
    while f >= 97 and l <= 8:
        moves.add(chr(f) + "" + str(l))
        f -=1
        l +=1
    return pawn in moves

print(solution("h1", "h3"))