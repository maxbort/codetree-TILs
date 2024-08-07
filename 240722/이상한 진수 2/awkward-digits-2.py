# a = list(input())

# one_cnt = 0

# for i in a:
#     if i == '1':
#         one_cnt += 1

# if len(a) == one_cnt:
#     a[-1] = '0'
# else:
#     for i in range(len(a)):
#         if a[i] == '0':
#             a[i] = '1'
#             break

# b = ''.join(a)
# ans = 0

# for i in range(len(b)-1, -1, -1):
#     if b[i] == '1':
#         ans += 2 ** (len(b) - i - 1)
# print(ans)

import sys
a = list(map(int, list(input())))

ans = -sys.maxsize

for i in range(len(a)):
    a[i] = 1 - a[i]

    cnt = 0
    for j in range(len(a)):
        if a[j] == 1:
            cnt += 2 ** j
    
    ans = max(ans, cnt)

    a[i] = 1 + a[i]

print(ans)