import sys

input = sys.stdin.readline

n = int(input())

rank_change = [list(map(str,input().rstrip().split())) for _ in range(n)]

rank = {}
rank['A'] = 0
rank['B'] = 0

answer = 0
tmp = 'AB'
for user,score in rank_change:
    rank[user] += int(score)
    a_score = rank.get('A')
    b_score = rank.get('B')
    if a_score > b_score:
        if 'A' not in tmp:
            tmp = 'A'
            answer += 1

        else:
            if len(tmp) == 2:
                tmp = 'A'
                answer += 1

    elif b_score > a_score:
        if 'B' not in tmp:
            tmp = 'B'
            answer += 1

        else:
            if len(tmp) == 2:
                tmp = 'B'
                answer += 1
 
    else:
        if len(tmp) != 2:
            answer += 1
            tmp = 'AB'

    
print(answer)