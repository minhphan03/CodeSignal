# use index slicing 
# https://github.com/socathie/CodeFights/blob/master/Arcade/MirrorLake/DifferentSquares.py 
def solution(matrix):
    row = len(matrix)
    col = len(matrix[0])
    unique = []
    
    for i in range(row-1):
        for j in range(col-1):
            m = [
                    [matrix[i][j], matrix[i][j+1]],
                    [matrix[i+1][j], matrix[i+1][j+1]]
                ]
            if m not in unique:
                unique.append(m)
    return len(unique)

