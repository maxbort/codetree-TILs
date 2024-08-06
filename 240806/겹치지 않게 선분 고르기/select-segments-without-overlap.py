n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0

temp = [0] * 1001

for i in range(n):

    x,y = arr[i]
    cnt = 1

    for j in range(x,y):
        temp[j] = 1

    for j in range(n):
        if i == j:
            continue
        
        x,y = arr[j]
        flag = False

        for h in range(x,y):
            if temp[h] == 1:
                flag = True
                break
        
        if flag:
            continue
        
        cnt += 1
    
    ans = max(ans, cnt)
print(ans)