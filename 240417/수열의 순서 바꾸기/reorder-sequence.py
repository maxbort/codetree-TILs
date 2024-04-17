import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))

idx = n - 2

while idx >= 0 and num_list[idx] < num_list[idx+1]:
    idx -= 1
print(idx + 1)