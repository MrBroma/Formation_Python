# gestion des fuseau horaire depuis python 3.9
# utilisation de iana qui est la tz database

# UTC=échelle de temps pas un fuseau horaire

from datetime import datetime

now = datetime.now()

print(now.tzinfo)

from zoneinfo import ZoneInfo

now_in_vancouver = datetime.now(tz=ZoneInfo("America/Vancouver"))

print(now_in_vancouver)

now_in_montreal = datetime.now(tz=ZoneInfo("America/Montreal"))

print(now_in_montreal)

now_in_vancouver > now_in_montreal

now_in_paris = now_in_vancouver.astimezone(ZoneInfo("Europe/Paris"))

