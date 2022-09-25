from datetime import timedelta
from datetime import datetime


timedelta(days=20)

now = datetime.now()

now_in_15_days_minus_5_h = now + timedelta(days=15, hours=-5)

print(now)
print(now_in_15_days_minus_5_h)

feb_27_2022 = datetime(2022, 2, 27)

print(feb_27_2022 + timedelta(days=3))

