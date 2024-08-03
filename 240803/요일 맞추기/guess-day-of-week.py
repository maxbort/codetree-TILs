m1,d1,m2,d2 = map(int,input().split())

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_d1 = d1
for i in range(1,m1):
    total_d1 += num_of_days[i]

total_d2 = d2
for i in range(1,m2):
    total_d2 += num_of_days[i]

print(days[(total_d2 - total_d1) % 7])