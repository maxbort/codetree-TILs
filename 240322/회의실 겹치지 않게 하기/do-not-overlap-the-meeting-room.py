import sys

input = sys.stdin.readline

n = int(input())

m_list = [list(map(int,input().split())) for _ in range(n)]

m_list.sort(key=lambda x : (x[0],x[1]))

answer = 0
for i in range(n-1):
    now_s,now_e = m_list[i]
    check = 0
    for j in range(i+1,n):
        if check > 1:
            answer += 1
            break
        next_s,next_e = m_list[i+1]
        if next_s <= now_e and next_e <= now_e:
            check += 1
        else:
            break
        
print(answer)