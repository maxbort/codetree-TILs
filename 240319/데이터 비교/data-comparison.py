import sys

input = sys.stdin.readline

n = int(input())
num1 = list(map(int,input().split()))

m = int(input())
num2 = list(map(int,input().split()))

set_num1 = set(num1)

for i in num2:
    if i in set_num1:
        print("1", end=" ")
    else:
        print("0", end =" ")