# ✔Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔Напишите функцию, которая при запуске заменяет содержимое
# переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


data = [12, 3, 4, 5, 6]
starts = '23:34:10'
s = 'Буква S'
limits = (23, 56)


def solution():
    temp = globals().copy()
    for var, value in temp.items():
        if var.endswith('s') and len(var) > 1:
            globals()[var[:-1]] = value
            globals()[var] = None

solution()

print(data)
print(starts)
print(s)
print(limits)
print(start)
print(limit)