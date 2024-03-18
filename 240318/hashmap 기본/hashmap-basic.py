import sys

input = sys.stdin.readline

n = int(input())
com_list = [list(map(str,input().rstrip().split())) for _ in range(n)]

result = {}

for com in com_list:
    if com[0] == "add":
        result[com[1]] = com[2]
    if com[0] == "find":
        print(result.get(com[1]))
    if com[0] == "remove":
        result.pop(com[1])