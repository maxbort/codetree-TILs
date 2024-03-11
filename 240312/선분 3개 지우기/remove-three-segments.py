import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

line_list = [list(map(int,input().split())) for _ in range(n)]

line_num = [i for i in range(n)]
line_combi = list(combinations(line_num,3))

line_list.sort(key=lambda x : x[0])
answer = 0
for a,b,c in line_combi:
    tmp_list = []
    for i in range(n):
        if i == a or i == b or i == c:
            tmp_list.append([999,0])
        else:
            tmp_list.append(line_list[i])
    flag = True
    for i in range(n):
        end = tmp_list[i][1]
        for j in range(i+1,n):
            if end < tmp_list[j][0]:
                if tmp_list[j][1] != 0:
                    end = tmp_list[j][1]
            else:
                flag = False
                break
        if not flag:
            break
    if flag:
        answer += 1
print(answer)