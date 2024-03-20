import sys

input = sys.stdin.readline

n,g =map(int,input().split())

group=[list(map(int,input().split())) for _ in range(g)]
group.sort(key=lambda x : len(x))
invite = set()
invite.add(1)
flag = True
while flag:
    flag = False
    for i in group:
        k = i[0]
        num = i[1:]
        not_invite =[]
        for check in num:
            if check in invite:
                continue
            else:
                not_invite.append(check)
        if len(not_invite) == 1:
            invite.add(not_invite[0])
            flag = True
print(len(invite))