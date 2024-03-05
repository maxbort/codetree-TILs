import sys

input = sys.stdin.readline

bracket = list(map(str,input().rstrip()))

stack = []
answer = 0
n = len(bracket)
for i in range(n):
    check = True
    if bracket[i] == '(':
        stack.append(bracket[i])
        for k in range(i+1,n):
            if bracket[k] == '(':
                stack.append(bracket[k])
                for j in range(i+1,n):
                    if bracket[j] == ')':
                        stack.pop()
                    if not stack:
                        answer+= 1
                        check = False
                        break
                if stack:
                    print(answer)
                    exit()
                
            if not check:
                stack = []
                break
print(answer)