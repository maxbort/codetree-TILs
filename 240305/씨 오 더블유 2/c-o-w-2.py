import sys

input = sys.stdin.readline

n = int(input())
str_list = list(map(str,input().rstrip()))


answer = 0
for i in range(n):
    if str_list[i] == 'C':
        for j in range(i+1,n):
            if str_list[j] == 'O':
                for k in range(j+1,n):
                    if str_list[k] == 'W':
                        answer += 1
print(answer)