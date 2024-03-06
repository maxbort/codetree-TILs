import sys

input = sys.stdin.readline

n,m = map(int,input().split())

num_list1 = list(map(int,input().split()))
num_list2 = list(map(int,input().split()))

flag = True
answer = 0
for i in range(0,n-m+1):
    for j in range(m):
        if num_list2.count(num_list2[j]) == num_list1[i:i+m+1].count(num_list2[j]):
            continue
        else:
            flag = False
            break
    if flag:
        answer += 1

print(answer)