import sys

input = sys.stdin.readline

n = int(input())

people_list = list(map(str,input().split()))

# 버블정렬 아닌가?

swap = True
answer = 0
while swap:
    swap = False

    for i in range(n-1):
        if ord(people_list[i]) > ord(people_list[i+1]):
            people_list[i],people_list[i+1] = people_list[i+1],people_list[i]
            swap = True
            answer += 1
    
print(answer)