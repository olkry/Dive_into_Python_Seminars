# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# Пример использования.
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
#
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')

# def get_file_info(file_path):
#     parts = file_path.rsplit('/', 1)
#     path = parts[0] + '/' if len(parts) > 1 else ''
#
#     file_name_with_extension = parts[-1] if len(parts) > 1 else parts[0]
#     name, extension = file_name_with_extension.rsplit('.', 1) if '.' in file_name_with_extension else (
#     file_name_with_extension, '')
#
#     return path, name, '.' + extension if extension else ''
#
#
# # Пример использования
# file_path = '/home/user/docs/my.file.with.dots.txt'
# result = get_file_info(file_path)
# print(result)
#
# file_path = 'file_in_current_directory.txt'
# result = get_file_info(file_path)
# print(result)

# Решение автотеста:
def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)
