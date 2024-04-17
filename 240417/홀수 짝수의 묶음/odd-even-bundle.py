import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))

even = 0
odd = 0

for num in num_list:
    if num % 2 == 0:
        even+= 1
    else:
        odd+=1

if even == odd or even == odd + 1:
    print(even+odd)
else:
    if even > odd:
        while True:
            even -= 1
            if even == odd+1:
                break
        print(even + odd)
    else:
        while True:
            odd -= 2
            even += 1
            if even >= odd:
                break
            if even + 1 == odd:
                odd -= 2
                break
        

        print(odd+even)