import sys
n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0

def array_cnt(temp_arr):
    global max_val
    l = len(temp_arr)

    for i in range(0, l - 2):
        val = 0
        for j in range(3):
            val += temp_arr[i+j]
        max_val = max(max_val, val)

for i in range(n-1):
    for j in range(m-1):
        cnt = 0
        min_val = sys.maxsize
        for x in range(i,i+2):
            for y in range(j,j+2):
                cnt += arr[x][y]
                min_val = min(min_val, arr[x][y])
        
        max_val = max(max_val , cnt - min_val)

for i in range(n):
    array_cnt(arr[i])

    temp = []
    for j in range(n):
        temp.append(arr[j][i])
    
    array_cnt(temp)

print(max_val)