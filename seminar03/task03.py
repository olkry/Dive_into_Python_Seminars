# Задание №3
# Погружение в Python | Коллекции
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

data = (3, -8, 'sdg', 5.45, True, False, None, 6464, -988, 5.68, 5.21, 'gj')
my_dict = dict()

for item in data:
    t = type(item)
    if t in my_dict:
        my_dict[t].append(item)
    else:
        my_dict[t] = [item]
print(my_dict)
