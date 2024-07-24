n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def array_cnt(temp_arr):
    # l = len(temp_arr)
    
    # for i in range(0,l-m+1):
    #     cnt = 1
    #     for j in range(i+1,l):
    #         if temp_arr[i] == temp_arr[j]:
    #             cnt += 1
    #         else:
    #             break
    #     if cnt >= m:
    #         return True
    # return False
    seq_n, max_cnt = 1,1

    for i in range(1,n):
        if temp_arr[i] == temp_arr[i-1]:
            seq_n += 1
        else:
            seq_n = 1
        
        max_cnt = max(max_cnt, seq_n)
    
    return max_cnt >= m
            
        

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