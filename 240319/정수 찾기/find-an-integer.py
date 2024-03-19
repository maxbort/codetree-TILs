import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))

m = int(input())
m_list = list(map(int,input().split()))

set_n = set(n_list)
for i in m_list:
    if i in set_n:
        print("1")
    else:
        print("0")