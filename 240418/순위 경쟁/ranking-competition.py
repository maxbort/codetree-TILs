import sys

input = sys.stdin.readline

n = int(input())

score_list = {}
score_list['A'] = 0
score_list['B'] = 0
score_list['C'] = 0

award_list = ['A','B','C']

answer = 0
for _ in range(n):
    name, score = map(str,input().split())
    score_list[name] += int(score)
    max_score_list = [k for k,v in score_list.items() if max(score_list.values()) == v]
    if len(max_score_list) != len(award_list):
        answer += 1
        award_list = max_score_list
    else:
        for i in max_score_list:
            if i not in award_list:
                answer += 1
                break
        award_list = max_score_list
print(answer)