import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))

num_list.sort(key=lambda x : -abs(x))

m_list = []
p_list = []
for i in num_list:
    if i > 0 and len(p_list) < 3:
        p_list.append(i)
    elif i < 0 and len(m_list) < 2:
        m_list.append(i)
    
    if len(p_list) == 3 and len(m_list) == 2:
        break

tmp1 = 1
tmp2 = 1
for i in p_list:
    tmp1 *= i
if len(m_list) == 2:
    for j in m_list:
        tmp2 *= j
tmp2 *= p_list[0]

print(max(tmp1,tmp2))