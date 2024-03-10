import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

answer = -250000

def SquareSum(start_x,start_y,x_ran,y_ran):
    sum_return = 0
    for i in range(x_ran+1):
        for j in range(y_ran+1):
            sum_return += graph[start_x+i][start_y]
    return sum_return

for x in range(n):
    for y in range(m):
        for px in range(n):
            for py in range(m):
                tmp = -250000
                tmp1 = -250000
                tmp2 = -250000
                tmp3 = -250000
                if 0 <= x+px < n and 0<= y+py <m:
                    tmp = SquareSum(x,y,px,py)

                # 상단
                for x1 in range(n):
                    for y1 in range(0,y+1):
                        for px1 in range(n):
                            for py1 in range(m):
                                if 0 <= x1 + px1 < n and 0 <= y1 + py1 < y+py:
                                    tmp1 = SquareSum(x1,y1,px1,py1)
                                    answer= max(answer,tmp+tmp1)



                for x2 in range(0,x):
                    for y2 in range(y,y+py):
                        for px2 in range(n):
                            for py2 in range(m):
                                if 0 <= x2+px2 < x and y <= y2+py2 < y+py:
                                    tmp2 = SquareSum(x2,y2,px2,py2)
                                    answer = max(answer,tmp+tmp2)
                    
                for x3 in range(x,n):
                    for y3 in range(y,y+py):
                        for px3 in range(n):
                            for py3 in range(m):
                                if x <= x3+px3 < n and y <= y3+py3 < y+py:
                                    tmp3 = SquareSum(x3,y3,px3,py3)
                                    answer = max(answer,tmp+tmp3)
                
                for x4 in range(n):
                    for y4 in range(y+py,n):
                        for px4 in range(n):
                            for py4 in range(m):
                                if 0 <= x4+px4 <n and y+py < y4+py4 < n:
                                    tmp4 = SquareSum(x4,y4,px4,py4)
                                    answer = max(answer,tmp+tmp4)


print(answer)