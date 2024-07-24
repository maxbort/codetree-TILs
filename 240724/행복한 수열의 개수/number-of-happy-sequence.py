n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def array_cnt(temp_arr):
    length = len(temp_arr)
    cnt = 1
    idx = 1

    for i in range(idx, length):
        if temp_arr[i] == temp_arr[i-1]:
            cnt += 1
            if cnt >= m:
                return True
        else:
            if cnt >= m:
                return True
            else:
                cnt = 1
        idx += 1

    return False

val = 0
for i in range(n):
    if array_cnt(arr[i]):
        val += 1

    temp = []
    for j in range(n):
        temp.append(arr[j][i])
    
    if array_cnt(temp):
        val += 1
print(val)