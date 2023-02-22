import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.now().replace(microsecond=0))
print(datetime.datetime.now().replace(microsecond=0).isoformat())