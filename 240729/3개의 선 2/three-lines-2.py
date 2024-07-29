n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

arr.sort(key = lambda x : (x[0], x[1]))

x_s, y_s = set(), set()
for x,y in arr:
    x_s.add(x)
    y_s.add(y)

line=[]
for i in x_s:
    line.append((i,-1))
for i in y_s:
    line.append((-1,i))

l = len(line)

ans = 0
for i in range(l-2):
    for j in range(i+1, l-1):
        for h in range(j+1):
            flag = True
            for a, b in arr:
                if (line[i][0]==a or line[i][1]==b) or (line[j][0]==a or line[j][1]==b) or (line[h][0]==a or line[h][1]==b):
                    continue
                else:
                    flag = False
            
            if flag:
                ans = 1
print(ans)