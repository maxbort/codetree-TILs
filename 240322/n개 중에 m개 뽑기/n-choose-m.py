import sys

input = sys.stdin.readline

n,m = map(int,input().split())
answer = []


def print_answer():
    for i in answer:
        print(i, end = ' ')
    print()

def choose(num,cnt):
    if num == n+1:
        if cnt == m:
            print_answer()
        return
    
    answer.append(num)
    choose(num+1,cnt+1)
    answer.pop()
    
    choose(num+1,cnt)


choose(1,0)