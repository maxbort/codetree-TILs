import sys

input = sys.stdin.readline

n = int(input())

line_list = [list(map(int,input().split())) for _ in range(n)]
candi = []

answer = 0

def find_point(end_point,idx,candi):
    global answer
    if idx == n:
        answer = max(answer,len(candi))
        return

    if line_list[idx][0] > end_point:
        find_point(end_point,idx+1,candi)
        candi.append(line_list[idx])
        end_point=line_list[idx][1]
        find_point(end_point,idx+1,candi)
        candi.pop()
    else:
        find_point(end_point,idx+1,candi)

find_point(-1,0,candi)

print(answer)