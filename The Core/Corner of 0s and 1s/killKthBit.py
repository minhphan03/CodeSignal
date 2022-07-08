# The given number n the kth bit from the right was initially set to 0, but its current value might be different. 
# It's now up to you to write a function that will change the kth bit of n back to 0.

def solution(n, k):
    return n if len(bin(n).replace("0b", "")) < k else n - 2**(k-1) if bin(n).replace("0b", "")[-k] == "1" else n