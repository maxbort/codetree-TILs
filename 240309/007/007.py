import sys

input = sys.stdin.readline

class Secret:
    def __init__(self,secret_code,meeting,time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

secret_code, meeting_point, time = map(str,input().rstrip().split())
input_string = Secret(secret_code,meeting_point,time)

print("secret code :",input_string.secret_code)
print("meeting point :", input_string.meeting_point)
print("time :", input_string.time)