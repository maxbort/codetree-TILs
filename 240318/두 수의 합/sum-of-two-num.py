import sys
input = sys.stdin.readline

n,k = map(int,input().split())

num_list = list(map(int,input().split()))

sum_dict = {}
answer =0 
for i in num_list:
    a = k - i

    if a in sum_dict:
        answer += sum_dict[a]
    
    if i in sum_dict:
        sum_dict[i] += 1
    else:
        sum_dict[i] = 1
print(answer)