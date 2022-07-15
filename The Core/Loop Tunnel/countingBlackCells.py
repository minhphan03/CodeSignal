# resource from https://sites.google.com/site/tranquangtanqt1990/learn-code/codefights/arcade/2-the-core/level-4_10-count-black-cells
""" 
Imagine a white rectangular grid of n rows and m columns divided into two parts by a diagonal line running from the upper left to the lower right corner. Now let's paint the grid in two colors according to the following rules:

    A cell is painted black if it has at least one point in common with the diagonal;

    Otherwise, a cell is painted white.

Count the number of cells painted black. """
def solution(n, m):
    return n + m - 2 + gcd(n, m)

def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)
