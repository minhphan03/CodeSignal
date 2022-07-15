# https://qelifeblog.wordpress.com/2017/06/24/codefights-different-rightmost-bit/

def solution(n, m):
    return (n ^ m) & -(n ^ m)