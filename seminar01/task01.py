year = int(input('Enter year: '))

INTERLAYER_YEAR = 4
CENTURY = 100
QUATERCENTENARY = 400
result = year % INTERLAYER_YEAR == 0 and year % CENTURY != 0 or year % 400 == 0
print("Високосный год" if result else "Не високосный год")
