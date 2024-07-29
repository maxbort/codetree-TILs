a,b,c = map(int,input().split())

ans = 0
for i in range(1000):
    val = 0
    for j in range(1000):
        val = a * i + b * j

        if val <= c:
            if c - val <= c - ans:
                ans = val
        else:
            break

print(ans)