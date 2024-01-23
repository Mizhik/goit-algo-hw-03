import datetime as dt 
from datetime import datetime as dtdt , timedelta
#task 1
def get_days_from_today(date):
    try:
        f_date = dtdt.strptime(date, "%Y-%m-%d")
        today = dtdt.today()
        result = today - f_date
        return result.days
    except ValueError:
        return "Invalid date format, please enter 'YYYY-MM-DD' "

print(get_days_from_today("2021-10-09"))