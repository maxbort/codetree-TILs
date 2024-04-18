import sys

input = sys.stdin.readline

n = int(input())

answer = 0
tmp = []
for _ in range(n):
    right_check = float('inf')
    str_input = input().rstrip()
    for i in range(len(str_input)):
        if str_input[i] == ')':
            right_check = i
        if str_input[i] == '(':
            right_check+=1
    tmp.append([str_input,right_check])

tmp.sort(key=lambda x : -x[1])
result = ''
for i in tmp:
    result += i[0]

for i in range(len(result)):
    if result[i] == '(':
        for j in range(i,len(result)):
            if result[j] == ')':
                answer += 1
print(answer)