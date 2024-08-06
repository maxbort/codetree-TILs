import sys

n = int(input())
arr = list(map(int,input().split()))

min_val = sys.maxsize

total = sum(arr)
ans = []

def choose(idx, cnt):
    global min_val

    if idx == 2 * n:
        if cnt == n:
            min_val = min(min_val, abs(total - sum(ans) * 2))
        return
    
    ans.append(arr[idx])
    choose(idx+1, cnt+1)
    ans.pop()
    choose(idx+1, cnt)

choose(0,0)
print(min_val)