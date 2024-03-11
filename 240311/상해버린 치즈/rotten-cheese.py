import sys

input = sys.stdin.readline

n,m,d,s = map(int,input().split())

eat_when=[list(map(int,input().split())) for _ in range(d)]

sick_when = [list(map(int,input().split())) for _ in range(s)]

cheeze_list = [0 for _ in range(m+1)]
people_list = [i for i in range(n+1)]



for sick_pople,sick_time in sick_when:
    for people_num, cheeze_num, eat_time in eat_when:
        if people_num == sick_pople:
            if eat_time < sick_time:
                cheeze_list[cheeze_num] += 1


tmp = [0 for _ in range(m+1)]
for i in range(len(cheeze_list)):
    if cheeze_list[i]:
        for people_num,cheeze_num,eat_time in eat_when:
            if cheeze_num == i:
                for j in sick_when:
                    if people_num == j[0]:
                        tmp[i] += 1

k = max(tmp)
candi_list = []

for i in range(len(cheeze_list)):
    if cheeze_list[i] == k:
        candi_list.append(i)
tmp_list = [0 for _ in range(m+1)]
for i in candi_list:
    cnt = 0
    for people_num, cheeze_num, eat_time in eat_when:
        if i == cheeze_num:
            cnt+=1
    tmp_list[i] = cnt


print(max(tmp_list))