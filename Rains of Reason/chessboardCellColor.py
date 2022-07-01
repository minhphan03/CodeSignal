def solution(cell1, cell2):
    return color(cell1) == color(cell2)

def color(cell):
    if ((ord(cell[0]) % 2 == 1 and int(cell[1]) % 2 == 1) or 
        (ord(cell[0]) % 2 == 0 and int(cell[1]) % 2 == 0)) :
        return 0
    return 1
