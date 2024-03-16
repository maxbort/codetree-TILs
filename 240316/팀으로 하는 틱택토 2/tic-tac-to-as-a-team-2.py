import sys

input = sys.stdin.readline

result = [list(str(input().rstrip())) for _ in range(3)]
team_list =[]

answer= 0
for i in range(3):
    if i == 0:
        team1 = set(result[i])
        team2 = set([result[i][0], result[i+1][0], result[i+2][0]])
        if len(team1) == 2:
            if team1 not in team_list:
                answer += 1
                team_list.append(team1)
        if len(team2) == 2:
            if team2 not in team_list:
                answer += 1
                team_list.append(team2)
    if i== 2:
        team1 = set(result[i])
        team2 = set([result[i][2], result[i-1][2], result[i-2][2]])
        if len(team1) == 2:
            if team1 not in team_list:
                answer += 1
                team_list.append(team1)
        if len(team2) == 2:
            if team2 not in team_list:
                answer += 1
                team_list.append(team2)
    if i==1:
        team1 = set(result[i])
        team2 = set([result[i][1], result[i+1][1], result[i-1][1]])
        team3 = set([result[i-1][0], result[i][1], result[i+1][2]])
        team4 = set([result[i-1][2], result[i][1], result[i+1][0]])

        if len(team1) == 2:
            if team1 not in team_list:
                answer += 1
                team_list.append(team1)
        if len(team2) == 2:
            if team2 not in team_list:
                answer += 1
                team_list.append(team2)
        if len(team3) == 2:
            if team3 not in team_list:
                answer += 1
                team_list.append(team3)
        if len(team4) == 2:
            if team4 not in team_list:
                answer += 1
                team_list.append(team4) 
print(answer)