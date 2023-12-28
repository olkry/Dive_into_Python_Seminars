# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

def text_method(text):
    my_list = sorted(text.split())
    max_len = 0
    for item in my_list:
        if len(item) > max_len:
            max_len = len(item)
    for i, item in enumerate(my_list, start=1):
        print(i, item.rjust(max_len))


def text_method_2(text):
    indentation = 0
    words = text.split(' ')
    for word in words:
        if len(word) > indentation:
            indentation = len(word)
    for n, word in enumerate(words, 1):
        print(f'{n}. {word:>{indentation}}')



text = "hello beautiful world"

print(text_method(text))
print('-----------------')
print(text_method_2(text))
