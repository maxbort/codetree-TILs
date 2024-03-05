import sys

input = sys.stdin.readline

bracket = list(map(str,input()))
n = len(bracket)

answer = 0
for i in range(n):
    stack = []
    if bracket[i] == '(':
        stack.append(bracket[i])
        for j in range(i+1,n):
            if len(stack) == 1:
                stack.append(bracket[j])
            if bracket[j] == ')':
                if len(stack) == 2:
                    stack.append(bracket[j])
                if len(stack) == 3:
                    answer += 1
                    break

print(answer)