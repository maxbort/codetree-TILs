import sys

input = sys.stdin.readline

class UnLock:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code,color,second = map(str,input().split())

bomb = UnLock(code,color,second)

print("code :",bomb.code)
print("color :",bomb.color)
print("second :",bomb.second)