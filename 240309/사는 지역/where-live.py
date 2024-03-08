import sys

input = sys.stdin.readline

n = int(input())

class People:
    def __init__(self,name,address,location):
        self.name = name
        self.address = address
        self.location = location

pep = []
for _ in range(n):
    name,address,location = map(str,input().split())
    pep.append(People(name,address,location))

pep.sort(key=lambda x : x.name,reverse=True)
print("name",pep[0].name)
print("addr",pep[0].address)
print("city",pep[0].location)