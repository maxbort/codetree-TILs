n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

values = []


for i in range(n):
    for j in range(n):
        for k in range(n + 1):
            cnt = 0

            visited = [(i,j)]
            st = [(i,j)]

            while st:
                x,y = st.pop(0)

                if arr[x][y] == 1:
                    cnt += 1

                for dx, dy in zip(dxs,dys):
                    nx, ny = x + dx, y + dy
                    
                    if in_range(nx,ny) and abs(nx-i) + abs(ny-j) <= k and (nx,ny) not in visited:
                        visited.append((nx,ny))
                        st.append((nx,ny))

            if cnt * m >= 2 * k * (k + 1) + 1:
                values.append(cnt)


values.sort(reverse=True)

if len(values) == 0:
    print(0)
else:
    print(values[0])