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
            if bracket[j] == '(' and len(stack) == 1:
                stack.append(bracket[j])
            if bracket[j] == ')':
                if stack[-1] == '(' and len(stack) == 2:
                    stack.append(bracket[j])
                if stack[-1] == ')' and len(stack) == 3:
                    answer += 1
                    stack = []
                    break

print(answer)