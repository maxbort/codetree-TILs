import sys

input = sys.stdin.readline

n = int(input())
line = [list(map(int,input().split())) for _ in range(n)]

answer = float('inf')
for i in range(n):
    for j in range(n):
        if i== j:
            continue

        x1,y1= line[i]
        x2,y2=line[j]
        answer = min(answer,((abs((x1 - x2) * (x1 - x2))+ abs((y1 - y2) * (y1 - y2)))))

print(answer)