def solution(n):
    res = [[0 for i in range(n)] for j in range(n)]
    start = 1
    spiral(0, n-1, 0, n-1, start, res)
    return res

def spiral(row1, row2, col1, col2, start, matrix):
    if row1 > row2 or col1 > col2:
        return
    for i in range(col1, col2+1):
        matrix[row1][i] = start
        start +=1
    for i in range(row1+1, row2 +1):
        matrix[i][col2] = start
        start +=1
    if row1 != row2:
        for i in range(col2-1, col1-1, -1):
            matrix[row2][i] = start
            start +=1
    
    if col1 != col2:
        for i in range(row2-1, row1, -1):
            matrix[i][col1] = start
            start +=1
    
    spiral(row1+1, row2-1, col1+1, col2-1, start, matrix)