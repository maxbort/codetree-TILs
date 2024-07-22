import sys

n = int(input())
arr = [
    list(input())
    for _ in range(n)
]

max_val = -1

def carry(a,b,c):
    length = max(len(a),len(b),len(c))
    int_a = int(''.join(a))
    int_b = int(''.join(b))
    int_c = int(''.join(c))

    for i in range(length):
        d_a = int_a % 10
        d_b = int_b % 10
        d_c = int_c % 10

        if d_a + d_b + d_c >= 10:
            return True
        
        int_a //= 10
        int_b //= 10
        int_c //= 10
    
    return False
    

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not carry(arr[i], arr[j], arr[k]):
                max_val = max(max_val, int(''.join(arr[i])) + int(''.join(arr[j])) + int(''.join(arr[k])))
                
print(max_val)