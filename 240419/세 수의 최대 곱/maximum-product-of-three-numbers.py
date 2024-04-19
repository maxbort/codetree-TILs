import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))

num_list.sort(key=lambda x : -abs(x))

m_list = []
p_list = []

for i in num_list:
    if i >= 0 and len(p_list) < 3:
        p_list.append(i)
    elif i < 0 and len(m_list) < 3:
        m_list.append(i)
    
    if len(p_list) == 3 and len(m_list) == 3:
        break

tmp1,tmp2 = -float('inf'), -float('inf')

if len(m_list) == 1:
    tmp2 = 1
    tmp2 *= m_list[0]
    check = 0
    for j in range(n-1,0,-1):
        if num_list[j] >= 0:
            tmp2 *= num_list[j]
            check += 1
        if check == 2:
            break
    


elif len(m_list) >= 2:
    tmp2 = 1

    tmp2 *= m_list[0]
    tmp2 *= m_list[1]
    if p_list:
        tmp2 *= p_list[0]
    else:
        tmp2 *= m_list[2]

if len(p_list) == 1:
    tmp1 = 1

    tmp1 *= p_list[0]
    tmp1 *= m_list[0]
    tmp1 *= m_list[1]

elif len(p_list) == 2:
    tmp1 = 1
    tmp1 *= p_list[0]
    tmp1 *= p_list[1]
    for j in range(n-1,0,-1):
        if num_list[j] < 0:
            tmp1 *= num_list[j]
            break
elif len(p_list) == 3:
    tmp1 = 1
    tmp1 *= p_list[0]
    tmp1 *= p_list[1]
    tmp1 *= p_list[2]

print(max(tmp1,tmp2))