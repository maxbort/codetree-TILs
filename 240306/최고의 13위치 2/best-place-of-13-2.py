import sys

input = sys.stdin.readline

n = int(input())

coin_map = []
for _ in range(n):
    coin_map.append(list(map(int,input().split())))

answer = 0
for i in range(n):
    for j in range(n-2):
        tmp = 0
        for k in range(3):
            if coin_map[i][j+k] == 1:
                tmp += 1
        for a in range(i,n):
            if a==i:
                t = j+3
            else:
                t = j
            for b in range(t,n-2):
                tmp2 = 0
                for l in range(3):
                    if coin_map[a][b+l] == 1:
                        tmp2 += 1
                answer = max(answer,tmp+tmp2)
    
print(answer)