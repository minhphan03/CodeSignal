def solution(sequence):
    count = 0
    i = 0
    size = len(sequence)
    
    # special case of two first elements
    while len(sequence) >=2 and sequence[0] > sequence[1]:
        sequence.pop(0)
        count +=1
        size -=1
    
    #loop (check a trio of consecutive elements)
    while i < size -1:
        if sequence[i] >= sequence[i+1]:
            count +=1
            if sequence[i+1] <= sequence[i-1]:
                sequence.pop(i+1)
            else:
                sequence.pop(i)
                if i > 0:
                    i -= 1
            size = len(sequence)

        else:
            i +=1
    return True if count <=1 else False
            
