from datetime import datetime
from datetime import date

now=datetime.now()
cur_day=now.day
cur_month=now.month
cur_year=now.year
cur_hour=now.hour
cur_minute=now.minute
cur_timestamp=now.timestamp()

print(now.strftime("%m/%d/%Y, %H:%M:%S"))

date_string="5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

today=date(year=2022,month=5,day=5)
new_year=date(year=2023,month=1,day=1)
print(new_year-today)

print(date(year=1970,month=1,day=1)-today)

# u can use datetime for bookkeeping automation