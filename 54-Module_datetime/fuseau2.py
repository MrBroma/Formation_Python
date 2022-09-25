# lors de calcul on ne prend pas en compte heure ete et hiver

# EDT, EST
# Eastern Daylight Time
# Eastern Standard Time

from datetime import datetime
from zoneinfo import ZoneInfo

montreal_tz = ZoneInfo("America/Montreal")
march_7 = datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz)
march_8 = datetime(2020, 3, 8, 13, 0, 0, tzinfo=montreal_tz)
print(march_7.tzname())
print(march_8.tzname())

