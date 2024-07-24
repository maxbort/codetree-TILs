# import sys
# n,m = map(int,input().split())

# arr = [
#     list(map(int,input().split()))
#     for _ in range(n)
# ]

# max_val = 0

# def array_cnt(temp_arr):
#     global max_val
#     l = len(temp_arr)

#     for i in range(0, l - 2):
#         val = sum(temp_arr[i:i+3])
#         max_val = max(max_val, val)

# for i in range(n-1):
#     for j in range(m-1):
#         cnt = 0
#         min_val = sys.maxsize
#         for x in range(i,i+2):
#             for y in range(j,j+2):
#                 cnt += arr[x][y]
#                 min_val = min(min_val, arr[x][y])
        
#         max_val = max(max_val , cnt - min_val)

# for i in range(n):
#     array_cnt(arr[i])

# for i in range(m):
#     temp = []
#     for j in range(n):
#         temp.append(arr[j][i])
    
#     array_cnt(temp)

# print(max_val)


# 변수 선언 및 입력:

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 가능한 모든 모양을 전부 적어줍니다.
shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def grid_sum(x,y):
    max_val = 0

    for i in range(6):
        is_possible = True
        cnt = 0

        for dx in range(0,3):
            for dy in range(0,3):
                if shapes[i][dx][dy] == 0:
                    continue
                if not in_range(x+dx,y+dy):
                    is_possible = False
                else:
                    cnt += grid[x+dx][y+dy]
        
        if is_possible:
            max_val = max(max_val, cnt)
    
    return max_val

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, grid_sum(i,j))
print(ans)