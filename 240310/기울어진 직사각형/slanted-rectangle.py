# import sys

# input = sys.stdin.readline

# n = int(input())

# graph = [list(map(int,input().split())) for _ in range(n)]

# answer = 0

# for i in range(n):
#     for j in range(n):
#         tmp = 0
#         x,y = i,j
#         check1 = 0
#         check2 = 0
#         while True:
#             dx = x - 1
#             dy = y + 1
#             if 0 <= dx < n and 0 <= dy < n:
#                 if dx == 0 and dy == n-1:
#                     break
#                 check1+= 1
#                 tmp += graph[dx][dy]
#                 x,y = dx,dy
#             else:
#                 break

#         if check1 == 0:
#             continue

#         while True:
#             dx = x - 1
#             dy = y - 1
#             if 0 <= dx < n and 0 <= dy < n:
                
#                 tmp += graph[dx][dy]
#                 check2+= 1
#                 x,y = dx,dy
#             else:
#                 break

#         if check2 == 0:
#             continue
        
#         while check1 > 0:
#             dx = x + 1
#             dy = y - 1
#             if 0 <= dx < n and 0 <= dy < n:
#                 x,y = dx,dy
#                 check1 -= 1
#                 tmp += graph[dx][dy]
#             else:
#                 break
#         if check1 != 0:
#             continue

#         while check2 > 0:
#             dx = x + 1
#             dy = y + 1
#             if 0 <= dx < n and 0 <= dy < n:
#                 x,y = dx,dy
#                 tmp += graph[dx][dy]
#                 check2 -= 1
#             else:
#                 break

#         if check2 !=0:
#             continue
#         answer = max(answer,tmp)

# print(answer)


##############모범 답안
# 변수 선언 및 입력:

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def get_score(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]
    
    sum_of_nums = 0

    # 기울어진 직사각형의 경계를 쭉 따라가봅니다.
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy
                
            # 기울어진 직사각형이 경계를 벗어나는 경우라면
            # 불가능하다는 의미로 답이 갱신되지 않도록
            # 0을 반환합니다.
            if not in_range(x, y):
                return 0
            
            sum_of_nums += grid[x][y]
    
    return sum_of_nums


ans = 0

# (i, j)를 시작으로 1, 2, 3, 4 방향
# 순서대로 길이 [k, l, k, l] 만큼 이동하면 그려지는
# 기울어진 직사각형을 잡아보는
# 완전탐색을 진행해봅니다.
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, get_score(i, j, k, l))

print(ans)