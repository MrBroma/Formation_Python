from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# montreal_tz = ZoneInfo("America/Montreal")
# march_7 = datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz)
# march_8 = march_7 + timedelta(days=1)
#
#
# print(march_8)

# La meilleure méthode pour comparer des fuseau horaire --> UTC

montreal_tz = ZoneInfo("America/Montreal")
march_7 = datetime(2020, 3, 7, 13, 0, 0)
march_7_utc = march_7.astimezone(ZoneInfo("UTC"))


march_8 = march_7_utc + timedelta(days=1)
march_8 = march_8.astimezone(montreal_tz)


print(march_8)

