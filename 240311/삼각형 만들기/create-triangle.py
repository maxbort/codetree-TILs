import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

point_list = [list(map(int,input().split())) for _ in range(n)]

answer = 0
combi = [i for i in range(n)]

combi_point = list(combinations(combi,3))
for point in combi_point:
    x1,y1 = point_list[point[0]]
    x2,y2 = point_list[point[1]]
    x3,y3 = point_list[point[2]]

    if x1 == x2:
        if y1 == y3 or y2 == y3:
            answer = max(answer,abs(y2-y1) * abs(x2-x3))
    
    if x2 == x3:
        if y2 == y1 or y3 == y1:
            answer = max(answer, abs(y2-y3) * abs(x2-x1))

    if x1 == x3:
        if y1 == y2 or y3 == y2:
            answer = max(answer,abs(y1-y3) * abs(x1-x2))

        

print(answer)