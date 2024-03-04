import sys

input = sys.stdin.readline

problem = list(map(str,input()))

answer = 0
for i in range(len(problem)):
    if problem[i] == '(':
        for j in range(i,len(problem)):
            if problem[j] ==')':
                answer += 1

print(answer)