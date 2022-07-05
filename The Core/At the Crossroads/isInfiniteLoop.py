# Given integers a and b, determine whether the following pseudocode results in an infinite loop

def solution(a, b):
    return a > b or abs(a-b) % 2 == 1