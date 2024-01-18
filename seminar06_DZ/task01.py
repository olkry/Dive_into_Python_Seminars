def _leap_year(year: int):
    return bool(not year % 4 and year % 100 or not year % 400)


date_to_prove = '31.6.2022'

day, month, year = date_to_prove.split('.')
day_check = {
    '1': 31,
    '2': 29 if _leap_year(int(year)) else 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31
}

if 0 < int(year) < 10000 and 0 < int(month) < 13 and 0 < int(day) <= day_check[month]:
    print('True')
else:
    print('False')

# Autotest reserch
'''
from sys import argv


def is_leap(year: int):
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))


def valid(full_date: str):
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True


if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove))'''
