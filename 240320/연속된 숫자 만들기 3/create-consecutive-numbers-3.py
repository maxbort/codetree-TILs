import sys

input = sys.stdin.readline

a,b,c = map(int,input().split())

answer = 0
while True:
    if b-a == 1 and c-b == 1:
        break
    else:
        answer += 1
        if b-a > c-b:
            c = b-1
            b,c = c,b
        else:
            a = b+1
            a,b = b,a
        
print(answer)