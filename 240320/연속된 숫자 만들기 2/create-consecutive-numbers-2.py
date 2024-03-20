import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

answer = 0

while True:
    if b-a == 1 and c-b == 1:
        break
    else:
        if b-a < c-b:
            if b-a == 1:
                tmp = (b+c)//2
                a = tmp
                a,b = b,a
                answer += 1
            else:
                tmp = (a+b) // 2
                c = tmp
                b,c = c,b
                answer += 1
        else:
            if c-b == 1:
                tmp = (a+b)//2
                c = tmp
                b,c = c,b
                answer += 1
            else:
                tmp = (c+b) //2
                a = tmp
                a,b = b,a
                answer += 1

print(answer)