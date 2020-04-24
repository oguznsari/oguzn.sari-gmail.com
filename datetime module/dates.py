import datetime
import pytz

d = datetime.date(2016, 7, 24)      # date - year month date
tday = datetime.date.today()
print(d)
print(tday)
print(tday.year)
print(tday.day)

print(tday.weekday())               # m-0 to s-6
print(tday.isoweekday())            # m-1 to s-7

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)                # 1 week later
print(tday - tdelta)                # 1 week ago


bday = datetime.date(2021, 2, 28)
aybday = datetime.date(2020, 8, 17)
ayb1stday = datetime.date(2019, 8, 5)

till_bday = bday - tday
till_aybday = aybday - tday
timeframe = tday - ayb1stday

print(till_bday.days, till_aybday.days, timeframe.days)
print(till_bday.total_seconds())

t = datetime.time(9, 30, 45, 100000)               # hours, minutes, seconds and microseconds
print(t)
print(t.hour)


dt = datetime.datetime(2020, 4, 25, 1, 15, 45, 100000)      # y, m, d, h, m, s, ms
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)

tdelta = datetime.timedelta(days=7, hours=2)
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()                # allows us to pass timezone
dt_utcnow = datetime.datetime.utcnow()          # timezone aware datetime

print(dt_today)
print(dt_now)
print(dt_utcnow)


# timezone aware dt
dt = datetime.datetime(2020, 4, 25, 1, 15, 45, tzinfo=pytz.UTC)      # y, m, d, h, m, s, ms
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)
dt_mtn = dt_now.astimezone(pytz.timezone('Europe/Istanbul'))
print(dt_mtn)
# for tz in pytz.all_timezones:
#     print(tz)

# naive datetime local time - convert it to a tz aware
dt_mtn2 = datetime.datetime.now()
mtn2_tz = pytz.timezone('Europe/Istanbul')
dt_mtn2 = mtn2_tz.localize(dt_mtn2)
print(dt_mtn2)
print(dt_mtn2.isoformat())


print(dt_mtn2.strftime('%B %d, %Y'))

dt_str = 'April 25, 2020'
dtfromstr = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dtfromstr)

# strftime - Datetime to String
# strptime - String to Datetime
