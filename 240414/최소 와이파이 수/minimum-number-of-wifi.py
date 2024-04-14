import sys

input = sys.stdin.readline

n,m = map(int,input().split())

people_point = list(map(int,input().split()))

wifi_point = [False for _ in range(n)]

answer = 0
for i in range(n):
    if people_point[i] == 0:
        wifi_point[i] = True


for i in range(n):
    if not wifi_point[i]:
        answer += 1
        for j in range(i,i+2*m+1):
            if 0 <= j < n:
                wifi_point[j] = True
            if j >= n-1:
                print(answer)
                sys.exit()
print(answer)