n = int(input())

ans = 0
tmp = []

def beautiful():
    global tmp
    idx = 0

    while idx < n:
        if idx + tmp[idx] > n:
            return False

        for i in range(idx, idx + tmp[idx]):
            if tmp[i] != tmp[idx]:
                return False
        
        idx += tmp[idx]
    
    return True

def choose(cnt):
    global ans , tmp

    if cnt == n:
        if beautiful():
            ans += 1
        return

    for i in range(1,5):
        tmp.append(i)
        choose(cnt + 1)
        tmp.pop()

choose(0)
print(ans)