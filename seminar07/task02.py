# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint, choice

consonant = set([chr(i) for i in range(ord('а'), ord('я') + 1)])
vowels = list('уеаоэяийюё')
consonant = list(consonant.difference(set(vowels)))
first_consonant = list(set(consonant).difference(set(list('ьыъ'))))

MIN_NAME = 4
MAX_NAME = 7


def generate_name(count: int):
    result = []
    for _ in range(count):
        name = choice(first_consonant)
        for i in range(1, randint(MIN_NAME, MAX_NAME)):
            name += choice(vowels) if i % 2 else choice(consonant)
        result.append(name.title())
    with open('names.txt', 'w', encoding='UTF-8') as file:
        file.write('\n'.join(result))


generate_name(10)
