# approach from GeekstoGeeks
# https://www.geeksforgeeks.org/minimum-number-appends-needed-make-string-palindrome/

def solution(st):
    for i in range(len(st)):
        if isPalindrome(st[i:]):
            return st + st[0:i][::-1]

def isPalindrome(s):
    return s == s[::-1]