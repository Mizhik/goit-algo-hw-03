#task 1
import datetime as dt 
from datetime import datetime as dtdt , timedelta
def get_days_from_today(date):
    try:
        f_date = dtdt.strptime(date, "%Y-%m-%d")
        today = dtdt.today()
        result = today - f_date
        return result.days
    except ValueError:
        return "Invalid date format, please enter 'YYYY-MM-DD' "
print(get_days_from_today("2024-10-09"))
#
#task 2
#
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
#
#task 3
#
import re
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    pat = r"[\+\d]+"
    new_number =''.join(re.findall(pat, phone_number))
    if len(new_number)== 10:
        return "+38" + new_number
    elif len(new_number) == 12:
        return '+' + new_number
    else:
        return new_number

result = [normalize_phone(number) for number in raw_numbers]   
print("Нормалізовані номери телефонів для SMS-розсилки:", result)
#
#task 4
#
import datetime as dt
from datetime import datetime as dtdt

users = [
    {"name": "John Doe", "birthday": "1985.01.28"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(users=None):
    tdate = dtdt.today().date() 
    birthdays = [] 
    for user in users:  
        bdate = user["birthday"]  
        bdate = str(tdate.year) + bdate[4:]  
        bdate = dtdt.strptime(bdate, "%Y.%m.%d").date() 
        week_day = bdate.isoweekday()
        days_between = (bdate - tdate).days

        if 0 <= days_between < 7:  
            if week_day < 6: 
                birthdays.append({'name': user['name'], 'birthday': bdate.strftime("%Y.%m.%d")})
            else:
                if (bdate + dt.timedelta(days=1)).weekday() == 0:  
                    birthdays.append({'name': user['name'], 'birthday': (bdate + dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                elif (bdate + dt.timedelta(days=2)).weekday() == 0:
                    birthdays.append({'name': user['name'], 'birthday': (bdate + dt.timedelta(days=2)).strftime("%Y.%m.%d")})
        else:
            bdate = bdate.replace(year=tdate.year + 1)
            week_day = bdate.isoweekday()  
            if week_day < 6:
                birthdays.append({'name': user['name'], 'birthday': bdate.strftime("%Y.%m.%d")})
            else:
                if (bdate + dt.timedelta(days=1)).weekday() == 0:
                    birthdays.append({'name': user['name'], 'birthday': (bdate + dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                elif (bdate + dt.timedelta(days=2)).weekday() == 0:  
                    birthdays.append({'name': user['name'], 'birthday': (bdate + dt.timedelta(days=2)).strftime("%Y.%m.%d")})
    return birthdays

print("Список привітань на цьому тижні:",get_upcoming_birthdays(users))
