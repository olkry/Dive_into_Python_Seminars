# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.


items = {
    "спальник": 1.5,
    "палатка": 3.2,
    "термос": 0.6,
    "карта": 0.1,
    "фонарик": 0.3,
    "котелок": 0.8,
    "еда": 2.5,
    "одежда": 1.7,
    "обувь": 1.2,
    "нож": 0.2
}
max_weight = 7.0

def fill_backpack(items, max_weight):
    sorted_items = sorted(items.items(), key=lambda x: (x[1], x[0]), reverse=True)

    backpack = {}
    current_weight = 0

    for item, weight in sorted_items:
        if current_weight + weight <= max_weight and item not in backpack:
            backpack[item] = weight
            current_weight += weight
            max_weight -= weight  # обновление оставшейся грузоподъемности

    return backpack


backpack = fill_backpack(items, max_weight)
print(backpack)

# Код дерьмотестов:

# backpack = {}
#
# for item, weight in items.items():
#     if weight <= max_weight:
#         backpack[item] = weight
#         max_weight -= weight