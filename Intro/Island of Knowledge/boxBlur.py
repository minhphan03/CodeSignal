import numpy

def solution(image):
    height = len(image)
    width = len(image[0])
    a = numpy.zeros((height-2, width-2), dtype=int)
    for r in range(height-2):
        for c in range(width-2):
            a[r,c] = int((sum(image[r][c:c+3]) + sum(image[r+1][c:c+3]) + 
                        sum(image[r+2][c:c+3]))/9)
    return a.tolist()
