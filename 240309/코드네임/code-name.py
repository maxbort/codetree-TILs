import sys

input = sys.stdin.readline

class Agent:
    def __init__(self,name,score):
        self.name = name
        self.score = score

agent_list = []
for _ in range(5):
    agent_import = tuple(map(str,input().split()))
    agent_list.append(Agent(agent_import[0],agent_import[1]))

agent_list.sort(key=lambda x : int(x.score))

print(agent_list[0].name,agent_list[0].score)