import sys

input = sys.stdin.readline

class User:
    def __init__(self,user_id = "codetree",user_level=10):
        self.user_id = user_id
        self.user_level = user_level

user,level = map(str,input().split())

user1 = User()
user2 = User(user,int(level))

print("user", user1.user_id, "lv",user1.user_level)
print("user", user2.user_id, "lv",user2.user_level)