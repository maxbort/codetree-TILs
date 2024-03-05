import sys

input = sys.stdin.readline

bracket = list(map(str,input()))
n = len(bracket)

answer = 0
for i in range(n):
    check = False
    if bracket[i] == '(':
        check = True
        for j in range(i+1,n):
            if not check:
                break
            if bracket[j] == '(':
                for k in range(j+1,n):
                    if not check:
                        break
                    if bracket[k] == ')':
                        for l in range(k+1,n):
                            if not check:
                                break
                            if bracket[l] == ')':
                                answer += 1
                                check = False
                                break

print(answer)