import datetime

d0 = datetime.datetime(2022, 6, 15, 12, 0, 0)
d1 = datetime.datetime(2022, 6, 18, 15, 30, 0)
delta = (d1 - d0).total_seconds()
print(delta)