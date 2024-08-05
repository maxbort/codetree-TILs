n,k,p,t = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(t)
]

arr.sort(key = lambda x : x[0])

handShake = [0] * (n+1) # k번 이상 악수했는지 체크용
virus = [0] * (n+1) # 감염되면 1
virus[p] = 1

for t,x,y in arr:
    #print(t,x,y)
    if virus[x] == 1:
        if handShake[x] < k:
            virus[y] = 1
            handShake[x] += 1
    if virus[y] == 1:
        if handShake[y] < k:
            virus[x] = 1
            handShake[y] += 1
    #print("virus ---->", virus)
    #print("handShake ---->", handShake)
    

for i in range(1,n+1):
    print(virus[i],end='')