import sys

input = sys.stdin.readline

n = int(input())

com = set()

for _ in range(n):
    command, value = input().rstrip().split()
    value = int(value)

    if command == "find":
        if value in com:
            print("true")
        else:
            print("false")
    
    if command == "add":
        com.add(value)
    if command == "remove":
        com.remove(value)