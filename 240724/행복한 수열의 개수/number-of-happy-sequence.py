n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def array_cnt(temp_arr):
    length = len(temp_arr)
    
    for i in range(length-1, 0, -1):
        cnt = 1
        for j in range(i-1,-1,-1):
            if temp_arr[i] == temp_arr[j]:
                cnt += 1
                if cnt >= m:
                    return True
            else:
                if cnt >= m:
                    #print("yes temp_arr : {}".format(temp_arr))
                    return True
                else:
                    break
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