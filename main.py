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
#print(get_days_from_today("2024-10-09"))
#task 2
import random
def get_numbers_ticket(min, max, quantity):
    if (min >= 1 and max <= 1000)and (quantity <= (max - min)):
        list = []
        while len(list)<quantity:
            a = random.randint(min,max)
            if a not in list:
                list.append(a)
    return list

lottery_numbers = get_numbers_ticket(1, 48, 6)
print("Ваші лотерейні числа:", lottery_numbers)