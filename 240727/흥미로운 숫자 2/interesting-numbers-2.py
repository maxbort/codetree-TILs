from collections import Counter

x,y= map(int,input().split())

cnt = 0
for i in range(x,y+1):
    counter = Counter(list(str(i)))

    if len(dict(counter)) != 2:
        continue
    
    one_cnt = 0 
    for j in dict(counter).values():
        if j == 1:
            one_cnt += 1
    
    if one_cnt == 1:
        cnt += 1
print(cnt)