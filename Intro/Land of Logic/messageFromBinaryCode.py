def solution(code):
    result = ''
    for i in range(len(code) // 8):
        result += chr(int(code[i*8:(i+1)*8],2))
    return result