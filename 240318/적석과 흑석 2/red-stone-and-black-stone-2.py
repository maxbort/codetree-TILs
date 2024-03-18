from sortedcontainers import SortedSet

c,n = tuple(map(int,input().split()))

red_stone = [int(input()) for _ in range(c)]
black_stone = [tuple(map(int,input().split())) for _ in range(n)]

red_s = SortedSet(red_stone)
black_stone.sort(key=lambda x : x[1])

answer = 0

for a,b in black_stone:
    idx = red_s.bisect_left(a)
    if idx != len(red_s):
        ti = red_s[idx]

        if ti <= b:
            answer += 1
            red_s.remove(ti)

print(answer)