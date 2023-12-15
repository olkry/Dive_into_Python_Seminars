space = ' '
star = '*'

rows = int(input('Сколько ярусов елки: '))
spaces = rows - 1
stars = 1

for i in range(rows):
    print((space * spaces) + (star * stars))
    stars += 2
    spaces -= 1
