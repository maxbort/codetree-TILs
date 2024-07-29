import sys

n = int(input())
arr = list(map(int,input().split()))

min_cnt = sys.maxsize

for i in range(n):
    arr[i] *= 2

    for j in range(n):
        temp = []

        for h in range(n):
            if j == h:
                continue
            
            temp.append(arr[h])
        
        cnt = 0
        for h in range(n-2):
            cnt += abs(temp[h+1] - temp[h])
        
        min_cnt = min(min_cnt, cnt)
    
    arr[i] //= 2
print(min_cnt)