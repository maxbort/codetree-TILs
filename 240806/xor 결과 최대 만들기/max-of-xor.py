n,m = map(int,input().split())

ans = []
max_val = 0

def Print():
    global max_val

    data = 0
    for e in ans:
        data ^= e
    
    max_val = max(max_val, data)


def choose(idx, cnt):
    if idx == n+1:
        if cnt == m:
            Print()
        return
    
    ans.append(idx)  
    choose(idx + 1, cnt+1)
    ans.pop()
    choose(idx + 1, cnt)
            
choose(1,0)
print(max_val)