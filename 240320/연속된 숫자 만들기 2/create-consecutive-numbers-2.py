import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

answer = 0

if b-a == 1 and c-b == 1:
    print(answer)
if b-a == 2 or c-b == 2:
    print(1)
else:
    print(2)