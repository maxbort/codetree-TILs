import sys
input = sys.stdin.readline

A,B,x,y = map(int,input().split())

a = abs(B-A)
b = abs(A-x) + abs(B-y)
c = abs(A-y) + abs(B-x)

print(min(a,b,c))