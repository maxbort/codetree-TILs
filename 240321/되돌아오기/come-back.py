import sys

input = sys.stdin.readline

n = int(input())
command = [list(map(str,input().rstrip().split())) for _ in range(n)]
x,y = 0,0


dir_set = {
    'N':0,
    'E':1,
    'S':2,
    'W':3
}
answer = 0
for d,cnt in command:
    cnt = int(cnt)

    for _ in range(cnt):
        if d == 'N':
            y += 1
            answer += 1
        elif d == 'E':
            x += 1
            answer += 1
        elif d == 'S':
            y -= 1
            answer += 1
        else:
            x -= 1
            answer += 1
        
        if x == 0 and y == 0:
            print(answer)
            sys.exit()
print(-1)