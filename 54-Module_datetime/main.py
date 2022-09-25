# calcul sec depuis l'epoch Unix (1 janv 1970 00:00)

# from time import time
# print(time())

# import datetime
from datetime import date, time, datetime
#
# d = date(year=2021, month=10, day=22)
#
# print(d)
#
# t = time(hour=10, minute=19, second=10)
# print(t)
#
# dt = datetime(year=2021, month=10, day=22, hour=10, minute=19, second=10, microsecond=100)
# print(dt)
#
# print(datetime.now())
#
# datetime.today()
# date.today()

now = datetime.now()
print(now)

date = date.today()
print(date)

now.hour
now.minute
now.second

today = date.today()
print(today)

tomorrow = today.replace(day=today.day + 1)
print(tomorrow)

# Pas utiliser car ce n'est pas une bonne méthode --> fuseau horaire ...

