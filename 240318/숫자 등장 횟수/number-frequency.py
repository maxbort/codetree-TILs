import sys

input = sys.stdin.readline

n,m = map(int,input().split())

n_dict = {}
n_list = list(map(int,input().split()))
for a in n_list:
    if a in n_dict:
        n_dict[a] += 1
    else:
        n_dict[a] = 1

command = list(map(int,input().split()))

for i in command:
    if i in n_dict:
        print(n_dict[a], end = " ")
    else:
        print(0, end =" ")