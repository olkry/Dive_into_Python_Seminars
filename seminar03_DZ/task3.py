# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def get_duplicates(lst):
    seen = {}
    duplicates = []

    for item in lst:
        if item in seen:
            seen[item] += 1
            if seen[item] == 2:
                duplicates.append(item)
        else:
            seen[item] = 1

    return duplicates

# Пример использования
lst = [1, 1, 1, 1, 1]
result = get_duplicates(lst)
print(result)

# Решение автотеста
duplicates = set()

for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)

result = list(duplicates)
print(result)