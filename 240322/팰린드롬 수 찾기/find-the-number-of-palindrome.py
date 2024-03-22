import sys

input = sys.stdin.readline

x,y = map(int,input().split())

answer=  0
for check in range(x,y+1):
    check = str(check)
    c_range = len(check)
    flag = True
    for i in range((c_range//2) + 1):
        if check[i] != check[-(i+1)]:
            flag = False
            break
    if flag:
        answer += 1
print(answer)