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
#안
# # 변수 선언 및 입력
# n = int(input())
# arr = [
# 	int(input())
# 	for _ in range(n)
# ]

# # 모든 쌍을 다 잡아봅니다.
# ans = -1
# for i in range(n):
# 	for j in range(i + 1, n):
# 		for k in range(j + 1, n):
# 			carry = False
			
# 			# 일의 자리에서 carry가 발생하는 경우
# 			if arr[i] % 10 + arr[j] % 10 + arr[k] % 10 >= 10:
# 				carry = True
			
# 			# 십의 자리에서 carry가 발생하는 경우
# 			if arr[i] % 100 // 10 + arr[j] % 100 // 10 + arr[k] % 100 // 10 >= 10:
# 				carry = True
			
# 			# 백의 자리에서 carry가 발생하는 경우
# 			if arr[i] % 1000 // 100 + arr[j] % 1000 // 100 + arr[k] % 1000 // 100 >= 10:
# 				carry = True
			
# 			# 천의 자리에서 carry가 발생하는 경우
# 			if arr[i] % 10000 // 1000 + arr[j] % 10000 // 1000 + arr[k] % 10000 // 1000 >= 10:
# 				carry = True
			
# 			if carry == False:
# 				ans = max(ans, arr[i] + arr[j] + arr[k]);

# print(ans)