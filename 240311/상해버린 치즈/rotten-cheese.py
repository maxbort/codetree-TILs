import sys

input = sys.stdin.readline

n,m,d,s = map(int,input().split())

eat_when=[list(map(int,input().split())) for _ in range(d)]

sick_when = [list(map(int,input().split())) for _ in range(s)]

cheeze_list = [False for _ in range(m+1)]
people_list = [i for i in range(n+1)]

for sick_pople,sick_time in sick_when:
    for people_num, cheeze_num, eat_time in eat_when:
        if people_num == sick_pople:
            if eat_time < sick_time:
                cheeze_list[cheeze_num] = True
            else:
                cheeze_list[cheeze_num] = False
    
answer = [0 for _ in range(n+1)]
for bad_cheeze in cheeze_list:
    if bad_cheeze:
        tmp = 0
        for people_num,cheeze_num,eat_time in eat_when:
            if cheeze_num == bad_cheeze:
                answer[people_num] += 1
print(max(answer))