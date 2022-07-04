# solution by CertainPerformance on StackOverflow
# https://stackoverflow.com/questions/66202105/how-do-i-get-arraymaxconsecutivesum-from-codesignal-more-efficient

def solution(inputArray, k):
    max_ = sum(inputArray[0:k])
    rollingSum = max_
    for i in range(len(inputArray)-k):
        rollingSum += inputArray[i+k]-inputArray[i]
        max_ = max(max_, rollingSum)
    return max_