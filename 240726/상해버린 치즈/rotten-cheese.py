n,m,d,s = map(int,input().split())

# 몇번째 사람, 몇번째 치즈, 언제 먹었어
eating_history = [
    list(map(int,input().split())) 
    for _ in range(d)
]

eating_history.sort(key = lambda x : x[2]) # 먹은 순서대로 정렬

# 몇번째 사람, 언제 아팠는지
sick_history = [
    list(map(int,input().split()))
    for _ in range(s)
]

sick_history.sort(key = lambda x : x[1]) # 아파지기 시작한 순서대로 정렬

max_pill = 0

possible_cheese = []
impossible_cheese = []

for i in sick_history:

    sick_person, sick_time = i

    for t in range(0, sick_time):

        for j in eating_history:

            ate_person, which_cheese, ate_time = j

            if sick_person == ate_person and t >= ate_time and which_cheese not in impossible_cheese:
                possible_cheese.append(which_cheese)

    for t in range(sick_time + 1, 101):
        for j in eating_history:

            ate_person, which_cheese, ate_time = j

            if sick_person == ate_person and t < ate_time:
                impossible_cheese.append(which_cheese)

                if which_cheese in possible_cheese:
                    possible_cheese.remove(which_cheese)





visited = [False for _ in range(51)]
for i in eating_history:
    person, cheese, _ = i

    if visited[person] == True:
        continue

    if cheese in possible_cheese:
        max_pill += 1
        visited[person] = True

print(max_pill)