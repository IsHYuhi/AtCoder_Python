import datetime

y = int(input())
m = int(input())
d = int(input())

ymd = datetime.datetime(y, m, d)
now = datetime.datetime(2014, 5, 17)
print((now-ymd).days)