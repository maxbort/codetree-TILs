import sys

input = sys.stdin.readline

n = int(input())

word_list = [str(input().rstrip()) for _ in range(n)]

answer = 0
di = {}
for i in range(n):
    word_list[i] = sorted(word_list[i])
    set_word = set(word_list[i])
    word_cnt = ""
    for k in set_word:
        word_cnt = word_cnt + k + str(word_list[i].count(k))
    if word_cnt in di:
        di[word_cnt] += 1
    else:
        di[word_cnt] = 1

a = di.values()
print(max(a))