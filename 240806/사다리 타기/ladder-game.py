import sys

n,m = map(int,input().split())

# arr = []
# for _ in range(m):
#     a, b = map(int, input().split())
#     arr.append((b, a - 1))

# arr.sort()

arr = [
    tuple(map(int,input().split()))
    for _ in range(m)
]

arr.sort(key = lambda x : x[1])

min_val = m
ans = []

def possible():
    num1 = [i for i in range(n+1)]
    num2 = [i for i in range(n+1)]

    for idx, _ in arr:
        num1[idx], num1[idx+1] = num1[idx+1], num1[idx]
    for idx, _ in ans:
        num2[idx], num2[idx+1] = num2[idx+1], num2[idx]
    
    for i in range(n):
        if num1[i] != num2[i]:
            return False
    return True

def choose(cnt):
    global min_val, ans

    if cnt == n:
        if possible():
            min_val = min(min_val, len(ans))
        return
    
    for i,j in arr:
        ans.append((i,j))
        choose(cnt+1)
        ans.pop()


choose(0)

print(min_val)