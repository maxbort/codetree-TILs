import sys

input = sys.stdin.readline

n = int(input())

num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_list.sort(reverse=True)
answer = -1

for i in range(n):
    tmp = num_list[i]
    for j in range(i+1,n):
        tmp = [int(number) for number in str(num_list[i])]
        tmp2 = [int(number) for number in str(num_list[j])]
        tmp.reverse()
        tmp2.reverse()
        check =True
        for k in range(len(tmp2)):
            a,b = int(tmp[k]), int(tmp2[k])
            if a+b > 9:
                check = False
                break
        if check:
            for l in range(j+1,n):
                tmp3 =[int(number) for number in str(num_list[i] + num_list[j])]
                tmp4 = [int(number) for number in str(num_list[l])]
                tmp3.reverse()
                tmp4.reverse()
                check2 = True
                for m in range(len(tmp4)):
                    c,d = int(tmp3[m]),int(tmp4[m])
                    if c+d > 9:
                        check2 = False
                        break
                if check2:
                    answer = max(answer, num_list[i] + num_list[j] + num_list[l]) 
print(answer)