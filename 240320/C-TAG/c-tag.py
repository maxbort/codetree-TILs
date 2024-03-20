import sys
from itertools import product,combinations

input = sys.stdin.readline

n, m = map(int,input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

answer=  0
s = set()

def check(x,y,z):
    s.clear()

    for i in range(n):
        s.add(A[i][x] + A[i][y] + A[i][z])

    for i in range(n):
        if (B[i][x] + B[i][y] + B[i][z]) in s:
            return False
        
    return True

for i in range(m-2):
    for j in range(i+1,m-1):
        for k in range(j+1,m):
            if check(i,j,k):
                answer += 1
print(answer)