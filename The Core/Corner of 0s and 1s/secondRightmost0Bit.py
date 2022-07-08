""" Presented with the integer n, find the 0-based position of the second rightmost zero bit in its binary representation (it is guaranteed that such a bit exists), counting from right to left.

You have to get rid of the rightmost 0
To fill in the rightmost 0 with 1 using x | (x + 1)
    10111100  (x)
|   10111101  (x + 1)
    --------
    10111101
Isolate the new rightmost 0
To isolate it use ~x & (x + 1)
// now x is the value after step 1

    10111101  (x)
    --------
    01000010  (~x)
&   10111110  (x + 1)
    --------
    00000010 """

def solution(n):
    return ~(n|(n+1)) & ((n|(n+1))+1)
