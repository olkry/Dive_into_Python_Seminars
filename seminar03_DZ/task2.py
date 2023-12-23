# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того,
# как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем. Отсортируйте по убыванию значения количества повторяющихся слов.


import re
from collections import Counter


def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    words = [word for word in words if not word.isdigit()]
    word_counts = Counter(words)
    top_words = word_counts.most_common(10)

    return top_words

text = 'Hello world. Hello Python. Hello again.'
result = top_10_words(text)
print(result)


# Вариант тестов
import re
from collections import Counter

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)