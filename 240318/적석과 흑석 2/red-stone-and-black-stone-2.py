import sys
from collections import deque

input = sys.stdin.readline

c, n = map(int,input().split())

red_stone = [int(input()) for _ in range(c)]
black_stone = [list(map(int,input().split())) for _ in range(n)]

red_stone.sort(reverse = True)
black_stone.sort(key=lambda x : (-x[1],-x[0]))
black_stone = deque(black_stone)

answer = 0
for i in red_stone:
    x,y = black_stone.popleft()
    if x <= i <= y:
        answer += 1
    else:
        black_stone.appendleft((x,y))

print(answer)