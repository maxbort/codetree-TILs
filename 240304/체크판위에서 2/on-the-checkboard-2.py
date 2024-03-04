import sys

input = sys.stdin.readline

r,c = map(int,input().split())

checkMap = []
for _ in range(r):
    checkMap.append(list(map(str,input().split())))

start = checkMap[0][0]

end = checkMap[-1][-1]
answer = 0
if start == end:
    print(answer)
else:
    for i in range(1,r-2):
        for j in range(1,c-2):
            if checkMap[i][j] != start:
                for k in range(i+1,r-1):
                    for l in range(j+1,c-1):
                        if checkMap[k][l] != end:
                            answer += 1
    print(answer)