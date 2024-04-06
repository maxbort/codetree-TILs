import sys

input = sys.stdin.readline

n = int(input())

rank_change = [list(map(str,input().rstrip().split())) for _ in range(n)]

rank = {}
rank['A'] = 0
rank['B'] = 0

answer = 0
tmp = ''
for user,score in rank_change:
    if rank[user] != int(score):
        rank[user] += int(score)
        a_score = rank.get('A')
        b_score = rank.get('B')
        if a_score > b_score:
            if 'A' not in tmp:
                tmp += 'A'
                answer += 1
            else:
                if len(tmp) == 2:
                    tmp = 'A'
                    anwer += 1
        
        elif b_score > a_score:
            if 'B' not in tmp:
                tmp += 'B'
                answer += 1
            else:
                if len(tmp) == 2:
                    tmp = 'B'
                    answer += 1
        else:
            if 'A' not in tmp or 'B' not in tmp:
                answer += 1
                tmp = 'AB'
print(answer)