import sys

input = sys.stdin.readline

n,m,d,s = map(int,input().split())

eat_when=[list(map(int,input().split())) for _ in range(d)]

sick_when = [list(map(int,input().split())) for _ in range(s)]

sick_when.sort(key=lambda x : x[1])
fisrt_sick = sick_when[0][1]
candi_bad_cheeze = [False for _ in range(m+1)]
cheeze_cnt = [0 for _ in range(m+1)]

for people_num, cheeze_num, eat_time in eat_when:
    for sick_people, sick_time in sick_when:
        if people_num == sick_people:
            if eat_time < sick_time:
                candi_bad_cheeze[cheeze_num] = True
                cheeze_cnt[cheeze_num] += 1

tmp = 0
bad_cheeze = 0
for i in range(len(cheeze_cnt)):
    if cheeze_cnt[i] > tmp:
        tmp = cheeze_cnt[i]
        bad_cheeze = i


answer = 0
for people_num, cheeze_num, eat_time in eat_when:
    if cheeze_num == bad_cheeze:
        answer += 1
print(answer)