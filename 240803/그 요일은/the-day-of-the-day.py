m1,d1,m2,d2 = map(int,input().split())
A = input()

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_d1 = d1
for i in range(1,m1):
    total_d1 += num_of_days[i]

total_d2 = d2
for i in range(1,m2):
    total_d2 += num_of_days[i]

total = (total_d2 - total_d1) // 7


for i in range((total_d2 - total_d1) % 7+1):
    if A == days[i]:
        total += 1
print(total)