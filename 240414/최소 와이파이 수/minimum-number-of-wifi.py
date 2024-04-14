import sys

input = sys.stdin.readline

n,m = map(int,input().split())

people_point = list(map(int,input().split()))

wifi_point = [False for _ in range(n)]

answer = 0
for i in range(n):
    if people_point[i] == 0:
        wifi_point[i] = True


for i in range(n):
    if not wifi_point[i]:
        answer += 1
        for j in range(i,i+2*m+1):
            if 0 <= j < n:
                wifi_point[j] = True
            if j >= n-1:
                print(answer)
                sys.exit()
print(answer)

## 모범답
# # 변수 선언 및 입력:
# n, m = tuple(map(int, input().split()))
# arr = list(map(int, input().split()))

# # 사람이 살고 있는 곳이 나오면
# # 와이파이를 해당 위치로부터 오른쪽으로 m만큼 떨어진 곳에 놓은 뒤,
# # 2m만큼 떨어진 곳에서 시작하여 다시 탐색을 진행합니다.
# cnt, i = 0, 0
# while i < n:
#     if arr[i] == 1:
#         cnt += 1
#         i += 2 * m + 1
#     else:
#         i += 1

# print(cnt)