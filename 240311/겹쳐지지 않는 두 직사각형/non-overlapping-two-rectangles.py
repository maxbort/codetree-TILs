# import sys

# input = sys.stdin.readline

# n,m = map(int,input().split())

# graph = []

# for _ in range(n):
#     graph.append(list(map(int,input().split())))

# answer = -250000

# def SquareSum(start_x,start_y,x_ran,y_ran):
#     sum_return = 0
#     if 0 <= start_x + x_ran < n and 0 <= start_y + y_ran<m:
#         for i in range(x_ran+1):
#             for j in range(y_ran+1):
#                 sum_return += graph[start_x+i][start_y+j]
#     else:
#         sum_return = - 250000
#     return sum_return

# for x in range(n):
#     for y in range(m):
#         for px in range(n):
#             for py in range(m):
#                 tmp = -250000
#                 tmp1 = -250000
#                 tmp2 = -250000
#                 tmp3 = -250000
#                 if 0 <= x+px < n and 0<= y+py <m:
#                     tmp = SquareSum(x,y,px,py)
#                 # 상단
#                 for x1 in range(n):
#                     for y1 in range(0,y):
#                         for px1 in range(n):
#                             for py1 in range(m):
#                                 tmp1 = -250000
#                                 if 0 <= x1 + px1 < n and 0 <= y1 + py1 < y:
#                                     tmp1 = SquareSum(x1,y1,px1,py1)
#                                     answer= max(answer,tmp+tmp1)


#                 # 좌측
#                 for x2 in range(0,x):
#                     for y2 in range(y,y+py+1):
#                         for px2 in range(n):
#                             for py2 in range(m):
#                                 tmp2 = -250000
#                                 if 0 <= x2+px2 < x and y <= y2+py2 <= y+py:
#                                     tmp2 = SquareSum(x2,y2,px2,py2)
#                                     answer = max(answer,tmp+tmp2)
#                 # 우측
#                 for x3 in range(x,n):
#                     for y3 in range(y,y+py+1):
#                         for px3 in range(n):
#                             for py3 in range(m):
#                                 tmp3 = -250000
#                                 if x <= x3+px3 < n and y <= y3+py3 <= y+py:
#                                     tmp3 = SquareSum(x3,y3,px3,py3)
#                                     answer = max(answer,tmp+tmp3)
#                 # 하단
#                 for x4 in range(n):
#                     for y4 in range(y+py+1,m):
#                         for px4 in range(n):
#                             for py4 in range(m):
#                                 tmp4 = -250000
#                                 if 0 <= x4+px4 < n and y+py < y4+py4 < m:
#                                     tmp4 = SquareSum(x4,y4,px4,py4)
#                                     answer = max(answer,tmp+tmp4)


# print(answer)


#### 모범 답안
import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
board = [
    [0 for _ in range(m)]
    for _ in range(n)
]


def clear_board():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0

            
def draw(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] += 1

            
def check_board():
    # 동일한 칸을 2개의 직사각형이 모두 포함한다면
    # 겹치게 됩니다.
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False


# (x1, y1), (x2, y2) 그리고
# (x3, y3), (x4, y4) 로 이루어져있는
# 두 직사각형이 겹치는지 확인하는 함수
def overlapped(x1, y1, x2, y2, x3, y3, x4, y4):
    clear_board()
    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)
    return check_board()


def rect_sum(x1, y1, x2, y2):
    return sum([
        grid[i][j]
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])


# 첫 번째 직사각형이 (x1, y1), (x2, y2)를 양쪽 꼭지점으로 할 때
# 두 번째 직사각형을 겹치지 않게 잘 잡아
# 최대 합을 반환하는 함수
def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = INT_MIN
    
    # (i, j), (k, l)을 양쪽 꼭지점으로 하는
    # 두 번째 직사각형을 정하여
    # 겹치지 않았을 때 중
    # 최댓값을 찾아 반환합니다.
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not overlapped(x1, y1, x2, y2, i, j, k, l):
                        max_sum = max(max_sum, 
                                      rect_sum(x1, y1, x2, y2) +
                                      rect_sum(i, j, k, l))
    
    return max_sum


# 두 직사각형을 잘 잡았을 때의 최대 합을 반환하는 함수
def find_max_sum():
    max_sum = INT_MIN
    
	# (i, j), (k, l)을 양쪽 꼭지점으로 하는
    # 첫 번째 직사각형을 정하여
    # 그 중 최댓값을 찾아 반환합니다.
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    max_sum = max(max_sum,
                                  find_max_sum_with_rect(i, j, k, l))
    return max_sum


ans = find_max_sum()
print(ans)