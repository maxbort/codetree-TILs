import sys

input = sys.stdin.readline

n = int(input())

seat = list(input().rstrip())
if n == 2:
    if '1' in seat:
        print(1)
        sys.exit()

dist = []
tmp = [0,1,0]
flag = False
for i in range(n):
    if seat[i] == '1':
        if flag:
            tmp[-1] = i
            dist.append(tmp)
            tmp = [i,1,0]
        else:
            flag = True
            tmp=[i,0,0]
    else:
        if flag:
            tmp[1]+= 1
first_p = 0
last_p = 0
for i in range(n):
    if seat[i] == '1':
        first_p = i
        break
for i in range(n-1,0,-1):
    if seat[i] == '1':
        last_p = i
        break

if dist:
    a= max(dist,key= lambda x : x[1])
    b = min(dist,key=lambda x : x[1])
    answer = b[1]
    new_one = (a[0]+a[2])//2

    if seat[0] == '0' and seat[1] =='0':
        answer = min(answer,new_one-a[0],a[2]-new_one)
        temp = min(b[1],first_p)
        answer = max(temp,answer)
    elif seat[-1] == '0' and seat[-2] =='0':
        answer = min(answer,new_one-a[0],a[2]-new_one)
        temp = min(b[1],n-last_p-1)
        answer = max(temp,answer)
    else:
        answer = min(answer,new_one-a[0],a[2]-new_one)
else:
    answer = 0
    answer = max(answer,first_p,n-last_p-1)

print(answer)

################## 모범답안
# import sys

# INT_MAX = sys.maxsize

# # 변수 선언 및 입력:
# n = int(input())
# seats = list(input())

# # Step1-1. 최적의 위치 찾기
# # 인접한 쌍들 중 가장 먼 1간의 쌍을 찾습니다.
# max_dist = 0
# max_i, max_j = -1, -1
# for i in range(n):
#     if seats[i] == '1':
#         for j in range(i + 1, n):
#             if seats[j] == '1':
#                 # 1간의 쌍을 골랐을 때
#                 # 두 좌석간의 거리가 지금까지의 최적의 답 보다 더 좋다면
#                 # 값을 갱신해줍니다.
#                 if j - i > max_dist:
#                     max_dist = j - i

#                     # 이때, 두 좌석의 위치를 기억합니다.
#                     max_i, max_j = i, j
                
#                 # 인접한 쌍을 찾았으므로 빠져나옵니다.
#                 break

# # Step1-2. 최적의 위치 찾기(예외 처리)
# # 만약 맨 앞 좌석이 비거나, 맨 뒷 좌석이 비어있는 경우의
# # 예외 처리를 해줍니다.
# max_dist2 = -1
# max_idx = -1
# # 맨 앞 좌석이 비어있을 때, 맨 앞 좌석에 배정하면
# # 거리가 얼마나 줄어드는지 확인합니다.
# if seats[0] == '0':
#     dist = 0
#     for i in range(0, n):
#         if seats[i] == '1':
#             break
#         dist += 1

#     if dist > max_dist2:
#         max_dist2 = dist
#         max_idx = 0

# # 맨 뒷 좌석이 비어있을 때, 맨 뒷 좌석에 배정하면
# # 거리가 얼마나 줄어드는지 확인합니다.
# if seats[n - 1] == '0':
#     dist = 0
#     for i in range(n - 1, -1, -1):
#         if seats[i] == '1':
#             break
#         dist += 1

#     if dist > max_dist2:
#         max_dist2 = dist
#         max_idx = n - 1


# # Step2. 최적의 위치에 1을 놓습니다.
# # 앞서 찾은 자리들 중 최적의 위치에 놓으면 됩니다.
# if max_dist2 >= max_dist // 2:
#     seats[max_idx] = '1'
# else:
#     seats[(max_i + max_j) // 2] = '1'


# # Step3. 이제 인접한 쌍들 중 가장 가까운 1간의 쌍을 찾습니다.
# # 이때의 값이 답이 됩니다.
# ans = INT_MAX
# for i in range(n):
#     if seats[i] == '1':
#         for j in range(i + 1, n):
#             if seats[j] == '1':
#                 ans = min(ans, j - i)

#                 # 인접한 쌍을 찾았으므로 빠져나옵니다.
#                 break

# print(ans)