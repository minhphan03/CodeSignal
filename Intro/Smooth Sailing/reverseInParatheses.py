# solution by Vineet Jain on StackOverflow using stacks
# https://stackoverflow.com/a/54473893

def solution(inputString):
    stack = []
    for x in inputString:
        if x == ")":
            temp = ""
            while stack[-1] != "(":
                # pop from last index
                temp += stack.pop()
            stack.pop() # pop the (
            for i in temp:
                stack.append(i)
        else:
            stack.append(x)
    return "".join(stack)

print(solution("foo((bar))"))