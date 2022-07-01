import numpy

def solution(matrix):
    height = len(matrix)
    width = len(matrix[0])
    result = numpy.zeros((height, width), dtype=int)
    for r in range(height):
        for c in range(width):
            count = 0
            # add nine values surrounding
            for rc in range(r-1, r+2):
                for cc in range(c-1, c+2):
                    if (0 <= rc < height) and (0 <= cc < width):
                        count += int(matrix[rc][cc])
            if matrix[r][c] == True:
                count -=1    
            result[r,c] = count
    return result.tolist()
