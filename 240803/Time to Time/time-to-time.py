a,b,c,d = map(int,input().split())

minute = 0

while True:
    if a == c and b == d:
        break

    b += 1
    minute += 1

    if b == 60:
        b = 0
        a += 1
print(minute)