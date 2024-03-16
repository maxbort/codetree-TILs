import sys

input = sys.stdin.readline

n = int(input())

input_str = str(input().rstrip())
answer = 0
for i in range(n+1):
    flag =True
    for j in range(n-1):
        check_str = input_str[j:j+i]
        for k in range(j+1,n):
            if check_str == input_str[k:k+i]:
                flag = False
    if flag:
        answer = i
        break

print(answer)