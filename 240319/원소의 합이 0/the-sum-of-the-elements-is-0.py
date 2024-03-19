import sys

input = sys.stdin.readline

n = int(input())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
c_list = list(map(int,input().split()))
d_list = list(map(int,input().split()))

dict_1 = {}
dict_2 = {}

for i in a_list:
    for j in b_list:
        a = i+j
        if a in dict_1:
            dict_1[a] += 1
        else:
            dict_1[a] = 1

for i in c_list:
    for j in d_list:
        a = i+j
        if a in dict_2:
            dict_2[a] += 1
        else:
            dict_2[a] = 1

answer = 0

for k,v in dict_1.items():
    want_know = -k
    if want_know in dict_2:
        tmp = dict_2[want_know]
        answer += v*tmp
print(answer)