n = int(input())
num = list(map(int, input().split()))
num.sort()

answer = 0

while len(num) > 1:
    tmp = []
    for i in range(0, len(num)-1, 2):
        tmp_sum = num[i] + num[i+1]
        answer += tmp_sum
        tmp.append(tmp_sum)
    if len(num) % 2 != 0:
        tmp.append(num[-1])
    num = tmp

if len(num) == 1:
    answer += num[0]

print(answer)