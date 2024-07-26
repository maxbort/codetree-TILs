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

for ate_person, which_cheese, ate_time in eating_history:
    flag = False
    for sick_person, sick_time in sick_history:
        if ate_person == sick_person:
            flag = True
            break
    if not flag:
        impossible_cheese.append(which_cheese)
        

for sick_person, sick_time in sick_history:
    
    for ate_person, which_cheese, ate_time in eating_history:

        for t in range(sick_time):

            if sick_person == ate_person and t > ate_time and which_cheese not in impossible_cheese:
                possible_cheese.append(which_cheese)

        for t in range(sick_time + 1, 101):

            if sick_person == ate_person and t < ate_time:
                impossible_cheese.append(which_cheese)

                if which_cheese in possible_cheese:
                    possible_cheese.remove(which_cheese)


# print(possible_cheese)
# print(impossible_cheese)

visited = [False for _ in range(51)]
for i in eating_history:
    person, cheese, _ = i

    # 이미 체크한 사람 제외
    if visited[person] == True: 
        continue

    if cheese in possible_cheese:
        max_pill += 1
        visited[person] = True

print(max_pill)