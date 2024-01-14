# ✔Создайте генератор чётных чисел от нуля до 100.
# ✔Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔Решение в одну строку.

gen_odd = (odd_num for odd_num in range(2, 101, 2) if sum(int(num) for num in str(odd_num)) != 8)
print(*gen_odd)
