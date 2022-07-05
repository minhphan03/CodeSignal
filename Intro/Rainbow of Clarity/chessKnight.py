# brute force
def solution(cell):
    moves = 0
    if checkPosition(chr(ord(cell[0])-2)+str(int(cell[1])+1)):
        moves +=1
    if checkPosition(chr(ord(cell[0])-2)+str(int(cell[1])-1)):
        moves +=1
    if checkPosition(chr(ord(cell[0])+2)+str(int(cell[1])+1)):
        moves +=1
    if checkPosition(chr(ord(cell[0])+2)+str(int(cell[1])-1)):
        moves +=1
    if checkPosition(chr(ord(cell[0])+1)+str(int(cell[1])+2)):
        moves +=1
    if checkPosition(chr(ord(cell[0])+1)+str(int(cell[1])-2)):
        moves +=1
    if checkPosition(chr(ord(cell[0])-1)+str(int(cell[1])+2)):
        moves +=1
    if checkPosition(chr(ord(cell[0])-1)+str(int(cell[1])-2)):
        moves +=1
    return moves

def checkPosition(c):
    if len(c) > 2:
        return False
    return ('a' <= c[0] <= 'h') and ('1' <= c[1:] <= '8')

# more elegant
def solution(cell):
    moves = 0
    x = [1, 1, -1, -1, 2, 2, -2, -2]
    y = [2, -2, 2, -2, 1, -1, 1, -1]
    for i in range(len(x)):
        if checkPosition(chr(ord(cell[0])+x[i])+str(int(cell[1])+y[i])):
            moves +=1
    return moves

print(solution('h8'))

# using list comprehension
def solution(c):
    x,y = ord(c[0])-96, int(c[1])
    return sum([1<=(x+i)<=8 and 1<=(y+j)<=8 for i in [-2,-1,1,2] for j in [-2,-1,1,2]])//2
