# ✔Самостоятельно сохраните в переменной строку текста.
# ✔Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔Напишите преобразование в одну строку.
# ✔Возьмите словарь, который вы получили. Сохраните его итераторатор.
# ✔Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

inp_string = input()
my_dict = {char: ord(char) for char in inp_string}
print(my_dict)

iter_dict = iter(my_dict.items())
for i in range(5):
    print(next(iter_dict))

