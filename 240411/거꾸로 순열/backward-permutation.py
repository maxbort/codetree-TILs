import sys

input = sys.stdin.readline

n = int(input())
visited = [False for _ in range(n+1)]
answer = []


def findPerRe(cur):

    if cur < 1:
        for i in answer:
            print(i, end= ' ')
        print()
        return
    
    for i in range(n,0,-1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)
        findPerRe(cur-1)

        answer.pop()
        visited[i] = False

findPerRe(n)