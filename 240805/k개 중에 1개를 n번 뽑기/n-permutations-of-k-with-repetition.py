k,n = map(int,input().split())
temp = []

def choose(cnt):
    global temp

    if cnt == n + 1:
        Print()
        return
    
    for i in range(1,k+1):
        temp.append(i)
        choose(cnt+1)
        temp.pop()

def Print():
    for i in temp:
        print(i, end=' ')
    print()
choose(1)