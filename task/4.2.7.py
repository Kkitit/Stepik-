import datetime
a,b = map(int, input().split())
date = datetime.date(2022,a,b)
date1 = date-datetime.timedelta(days=1)
date2 = date+datetime.timedelta(days=1)
print(f"{date1.strftime('%m.%d')} {date2.strftime('%m.%d')}")