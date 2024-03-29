import sys

input = sys.stdin.readline

n,m,d,s = map(int,input().split())

eat_when=[list(map(int,input().split())) for _ in range(d)]

sick_when = [list(map(int,input().split())) for _ in range(s)]

cheeze_list =[[] for _ in range(m+1)]

sick_cnt = 0
for people_num, cheeze_num, eat_time in eat_when:
    for sick_people, sick_time in sick_when:
        if people_num == sick_people:
            if eat_time < sick_time:
                cheeze_list[cheeze_num].append(people_num)
    


max_cnt = 0
for i in cheeze_list:
    if len(i) > max_cnt:
        max_cnt = max(len(i),max_cnt)

answer = 0

for i in range(len(cheeze_list)):
    tmp = 0
    visit=[False for _ in range(n+1)]
    if len(cheeze_list[i]) == max_cnt:
        for people_num, cheeze_num, eat_time in eat_when:
            if i == cheeze_num and not visit[people_num]:
                visit[people_num] = True
                tmp += 1
    answer = max(tmp,answer)
       
print(answer)