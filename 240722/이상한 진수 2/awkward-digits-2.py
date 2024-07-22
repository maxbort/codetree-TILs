a = list(input())

if len(a) == 1:
    a[0] = '0'
else:
    for i in range(len(a)):
        if a[i] == '0':
            a[i] = '1'
            break

b = ''.join(a)
ans = 0

for i in range(len(b)-1, -1, -1):
    if b[i] == '1':
        ans += 2 ** (len(b) - i - 1)
print(ans)