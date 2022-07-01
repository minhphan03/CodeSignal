def solution(matrix):
    sum = 0
    for col in range(len(matrix[0])):
        row = 0
        while row < len(matrix):
            if matrix[row][col] == 0:
                break
            else:
                sum += matrix[row][col]
            row += 1
    return sum