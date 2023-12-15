result = 0
TEN = 10
CENTURY = 100
THOUSAND = 1000
SQUARE = 2

while True:
    number = int(input('Введите число от 1 до 999: '))
    if number in range(1, 1000):
        if number < TEN:
            result = number ** SQUARE
        elif number >= TEN and number < CENTURY:
            num_1 = number // TEN
            num_2 = number % TEN
            result = num_1 * num_2
        else:
            first = number % TEN
            second = (number // TEN) % TEN
            third = number // CENTURY
            result = first * 100 + second * 10 + third
        break

print(result)
