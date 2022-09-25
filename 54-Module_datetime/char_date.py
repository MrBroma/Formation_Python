# Norme iso 8601
# YYYY-MM-DD

from datetime import datetime
print(datetime.fromisoformat("2021-10-24"))

# chaine de caractère en date
# parser
La_date = datetime.strptime("22 Oct 2021", "%d %b %Y")
print(La_date)

# date en texte --> strftime

now.sprftime("%d %B %Y")

from dateutil import parser

parser.parse("24 October 2021 at 9 am and 18 minutes")

# Bibliothèque très puissante

import dateparser

dateparser.parse("aujourd'hui")
dateparser.parse("demain")

dateparser.parse("Il y a un mois")

