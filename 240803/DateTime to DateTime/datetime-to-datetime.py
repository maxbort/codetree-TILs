a,b,c = map(int,input().split())

ans = 0

while True:
    if a == 11 and b == 11 and c == 11:
        break
    
    c -= 1
    ans += 1

    if c < 0:
        c = 59
        b -= 1

        if b < 0:
            b = 23
            c = 59
            a -= 1

if a > 11:
    ans = -1
elif a == 11 and b > 11:
    ans = -1
elif a == 1 and b == 11 and c > 11:
    ans = -1

print(ans)