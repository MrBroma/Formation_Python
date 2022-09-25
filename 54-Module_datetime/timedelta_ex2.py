from dateutil.relativedelta import relativedelta
from datetime import datetime


now = datetime.now()
now_in_2_months = now + relativedelta(months=2)

print(now_in_2_months)
