import sys

input = sys.stdin.readline

n = int(input())

answer = 0
num = list()

def find_bn():
    i = 0
    while i < n:
        if i + num[i] - 1 >= n:
            return False
        
        for j in range(i,i+num[i]):
            if num[i] != num[j]:
                return False
        
        i += num[i]
    return True

def cnt_bn(cnt):
    global answer

    if cnt == n:
        if find_bn():
            answer += 1
        return
    
    for i in range(1,5):
        num.append(i)
        cnt_bn(cnt+1)
        num.pop()

cnt_bn(0)
print(answer)