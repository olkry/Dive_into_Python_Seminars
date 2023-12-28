# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def key_params(**kwargs):
    return {str(value) if not isinstance(value, (int, float)) else value: key for key, value in kwargs.items()}

# Another variant

def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, str, float, bool, tuple)):
            result[value] = key
        else:
            result[str(value)] = key
    return result

params = key_params(a = 42,
b = 'hello',
c = 3.14,
d = 'world')
print(params)
