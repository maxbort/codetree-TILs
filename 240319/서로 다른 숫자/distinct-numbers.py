import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))

set_num = set(num_list)
print(len(set_num))