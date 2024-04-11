import sys

input = sys.stdin.readline

n = int(input())

visited = [False for _ in range(n+1)]

answer = []

def findPer(cur):
    if cur == n+1:
        for i in answer:
            print(i, end = ' ')
        print()
        return

    for i in range(1,n+1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)

        findPer(cur+1)

        answer.pop()
        visited[i] = False
    
findPer(1)