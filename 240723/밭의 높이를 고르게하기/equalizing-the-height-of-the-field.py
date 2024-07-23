n,h,t = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

gap = []

for i in arr:
    gap.append(abs(i-h))

#print(gap)

gap.sort()

cost = 0
for i in range(t):
    cost += gap[i] 
print(cost)