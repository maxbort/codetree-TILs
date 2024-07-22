import sys
n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

new_arr = arr[:]
for i in range(n):
    new_arr.append(arr[i])

min_cnt = sys.maxsize
for i in range(n):
    cnt = 0
    idx = 1
    for j in range(i,i+n-1):
        cnt += new_arr[j] * idx
        idx += 1
        
    min_cnt = min(min_cnt, cnt)

print(min_cnt)