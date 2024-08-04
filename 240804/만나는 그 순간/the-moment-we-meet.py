n,m = map(int,input().split())

A = [0] * 1001
B = [0] * 1001

a_idx = 1
time = 0

for i in range(n):
    d, t = input().split()
    t = int(t)
    time += t

    if d == 'R':
        for _ in range(t):
            A[a_idx] = A[a_idx - 1] + 1
            a_idx += 1
    else:
        for _ in range(t):
            A[a_idx] = A[a_idx - 1] - 1
            a_idx += 1


a_idx = 1

for i in range(m):
    d, t = input().split()
    t = int(t)

    if d == 'R':
        for _ in range(t):
            B[a_idx] = B[a_idx - 1] + 1
            a_idx += 1
    else:
        for _ in range(t):
            B[a_idx] = B[a_idx - 1] - 1
            a_idx += 1

cnt = -1
for i in range(1,time):
    if A[i] == B[i]:
        cnt = i
        break
print(cnt)