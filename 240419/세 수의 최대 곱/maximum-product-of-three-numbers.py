import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))

plus_list = []
minus_list = []
answer = 1
if len(num_list) == 3:
    for i in num_list:
        answer *= i
    print(answer)
    sys.exit()

for i in num_list:
    if i >= 0:
        plus_list.append(i)
    else:
        minus_list.append(i)
plus_list.sort(reverse=True)
minus_list.sort()

check = 0
if len(minus_list) == 0:
    for i in plus_list:
        answer *= i
        check += 1
        if check == 3:
            print(answer)
            sys.exit()

elif len(minus_list) == 1:
    for i in plus_list:
        answer *= i
        check += 1
        if check == 3:
            print(answer)
            sys.exit()

elif len(minus_list) == 2:
    tmp1 = 1
    tmp2 = 1
    tmp1 *= minus_list[0]
    tmp1 *= minus_list[1]
    tmp1 *= plus_list[0]
    if len(plus_list) > 2:
        for i in plus_list:
            tmp2 *= i
            check += 1
            if check == 3:
                answer = max(tmp1,tmp2)
                print(answer)
                sys.exit()
                

else:
    if len(plus_list) >= 3:
        tmp1 = minus_list[0] * minus_list[1] * plus_list[0]
        tmp2 = plus_list[0] * plus_list[1] * plus_list[2]
        print(max(tmp1,tmp2))
        sys.exit()
    
    elif 0 < len(plus_list) < 3:
        print(minus_list[0] * minus_list[1] * plus_list[0])
        sys.exit()
    else:
        print(minus_list[-1]*minus_list[-2]*minus_list[-3])
        sys.exit()