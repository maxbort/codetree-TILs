n = int(input())

block = []
for _ in range(n):
    block.append(int(input()))

answer = 0

block.sort()
std = sum(block) // n

end = n-1
start = 0

answer = -1
while end > start:
    max_block = block[end]
    min_block = block[start]

    if min_block == std:
        start += 1
    if max_block == std:
        end -= 1
    
    block[end] -= 1
    block[start] += 1
    answer += 1

print(answer)