import csv
import os
import json
import pprint

project_directory = os.getcwd()
csv_file_path = 'data/books.csv'
json_file_path = 'data/users.json'

absolute_path_csv = os.path.join(project_directory, csv_file_path)
absolute_path_json = os.path.join(project_directory, csv_file_path)



# with open(absolute_path_csv, 'r', newline='', encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     print(type(csv_reader))
#     for row in csv_reader:
#         print(row)


#
# with open(json_file_path, 'r', encoding='utf-8') as json_file:
#     # Загружаем данные из файла
#     data = json.load(json_file)
#
#     # Теперь переменная 'data' содержит данные из файла JSON
#     pprint.pprint(data)

















# Загрузим данные о пользователях из JSON-файла
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    users_data = json.load(json_file)

# Создадим пустой словарь для хранения данных пользователей
user_data_dict = {user['name']: user for user in users_data}

# Загрузим книги из файла books.csv
with open(absolute_path_csv, 'r', newline='', encoding='utf-8') as books_file:
    books_reader = csv.reader(books_file)
    next(books_reader)  # Пропустим заголовок

    # Создадим пустые массивы книг для каждого пользователя
    user_books = {user['name']: [] for user in users_data}

    # Распределим книги между пользователями
    for row in books_reader:
        book = {
            "title": row[0],
            "author": row[1],
            "pages": int(row[3]),
            "genre": row[2],
        }

        # Итерируем по пользователям и добавляем книгу каждому
        for user_name, user_books_list in user_books.items():
            user_books_list.append(book)

# Обновим данные о пользователях в соответствии с распределенными книгами
for user_name, books in user_books.items():
    if user_name in user_data_dict:
        user_data_dict[user_name]['books'] = books

# Теперь user_data_dict содержит обновленные данные о пользователях с информацией о книгах, распределенных "максимально поровну"
# Преобразуем результат в JSON и сохраним в файл
with open('output.json', 'w', encoding='utf-8') as output_file:
    json.dump(list(user_data_dict.values()), output_file, ensure_ascii=False, indent=2)
