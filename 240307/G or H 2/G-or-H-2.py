import sys

input = sys.stdin.readline

n = int(input())

point_list = ['O' for _ in range(101)]

for _ in range(n):
    point, alpha = map(str,input().split())
    point_list[int(point)] = alpha

answer = 0
a = 0
for i in range(101):
    if point_list[i] == 'G' or point_list[i] == 'H':
        for j in range(i,101):
            if point_list[j] == 'G' or point_list[j] == 'H':
                if point_list[i:j+1].count('G') == point_list[i:j+1].count('H'):
                    tmp = j-i
                    answer = max(answer,tmp)
print(answer)