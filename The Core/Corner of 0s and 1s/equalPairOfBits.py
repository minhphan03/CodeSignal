def solution(m, n):
    return ~(m^n) & -(~(m^n))