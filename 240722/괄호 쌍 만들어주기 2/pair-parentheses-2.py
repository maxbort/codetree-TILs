string = input()

cnt = 0
for i in range(1,len(string)):
    for j in range(i+2, len(string)):
        if (string[i-1] == string[i] == '(') and (string[j-1] == string[j] == ')'):
            cnt += 1

print(cnt)