import sys

input = sys.stdin.readline

n, m, d, s = map(int, input().split())

# 사람이 먹은 치즈와 그 시간을 기록
eat_when = [list(map(int, input().split())) for _ in range(d)]

# 아픈 기록을 사전에 정렬
sick_when = sorted([list(map(int, input().split())) for _ in range(s)], key=lambda x: x[1])

# 각 치즈별로 먹은 사람을 기록할 리스트
cheeze_list = [[] for _ in range(m+1)]

# 각 사람이 아프기 시작한 최소 시간을 기록
min_sick_time = [sys.maxsize for _ in range(n+1)]
for people_num, sick_time in sick_when:
    min_sick_time[people_num] = min(min_sick_time[people_num], sick_time)

# 아픈 시간 전에 먹은 치즈만을 후보로 선정
for people_num, cheeze_num, eat_time in eat_when:
    if eat_time < min_sick_time[people_num]:
        cheeze_list[cheeze_num].append(people_num)

# 가장 많이 아픈 사람들이 먹은 치즈 찾기
max_eaters = 0
for cheeze_eaters in cheeze_list:
    unique_eaters = len(set(cheeze_eaters))  # 중복 제거
    max_eaters = max(max_eaters, unique_eaters)

print(max_eaters)