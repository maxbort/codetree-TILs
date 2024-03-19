import sys

input = sys.stdin.readline

n = int(input())

word_list = [str(input().rstrip()) for _ in range(n)]

answer = 0
for i in range(n):
    set_word = set(word_list[i])
    tmp = 1
    for j in range(i+1,n):
        flag = True
        for k in set_word:
            if word_list[i].count(k) != word_list[j].count(k):
                flag = False
                break
        if flag:
            tmp += 1
        
    answer = max(answer,tmp)


print(answer)