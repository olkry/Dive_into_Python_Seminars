from fractions import Fraction


def calculate_fractions(frac1, frac2):
    # Разбиваем строки на числитель и знаменатель
    numerator1, denominator1 = map(int, frac1.split('/'))
    numerator2, denominator2 = map(int, frac2.split('/'))

    # Создаем объекты Fraction
    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)

    # Вычисляем сумму и произведение дробей
    sum_result = fraction1 + fraction2
    product_result = fraction1 * fraction2

    return sum_result, product_result


frac1 = input('Введите первую дробь (в формате a/b): ')
frac2 = input('Введите вторую дробь (в формате a/b): ')

result_sum, result_product = calculate_fractions(frac1, frac2)
print('Сумма дробей:', result_sum)
print('Произведение дробей:', result_product)
print('Сумма дробей:', result_sum)
print('Произведение дробей:', result_product)

# Решени автотестов:


from fractions import Fraction

# frac1 = '2/5'
# frac2 = '3/5'

# Разбиваем строки на числитель и знаменатель без использования map
numerator1_str, denominator1_str = frac1.split('/')
numerator2_str, denominator2_str = frac2.split('/')

# Преобразуем строки в целые числа
numerator1 = int(numerator1_str)
denominator1 = int(denominator1_str)
numerator2 = int(numerator2_str)
denominator2 = int(denominator2_str)

common_denominator = denominator1 * denominator2

new_numerator1 = numerator1 * denominator2
new_numerator2 = numerator2 * denominator1

summation_numerator = new_numerator1 + new_numerator2
multiplication_numerator = numerator1 * numerator2

print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")

# Преобразуем введенные строки в объекты Fraction
fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

# Вычисляем сумму и произведение дробей
summation = fraction1 + fraction2
multiplication = fraction1 * fraction2

print(f"Сумма дробей: {summation}")
print(f"Произведение дробей: {multiplication}")
