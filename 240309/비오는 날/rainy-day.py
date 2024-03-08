import sys

input = sys.stdin.readline

class Weather:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
news = []
for _ in range(n):
    date,day,weather = map(str,input().split())
    news.append(Weather(date,day,weather))

news.sort(key=lambda x : x.date)

for i in news:
    if i.weather == "Rain":
        print(i.date,i.day,i.weather)
        break