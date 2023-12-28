# ✔Напишите функцию, которая принимает строку текста.
# ✔Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def chars(text):
    new = []
    for i in set(text):
        new.append(ord(i))
    return sorted(new, reverse=True)


print(chars('age 7iy3 c37f pale 345'))
