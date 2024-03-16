import sys

input = sys.stdin.readline

n = int(input())

req = [list(map(int,input().split())) for _ in range(n)]

req.sort(key=lambda x : x[1])

end_time = 0
answer = 0
for meet in req:
    if meet[0] >= end_time:
        answer += 1
        end_time= meet[1]
print(answer)