import csv

# Замените 'absolute_path_users.csv' и 'absolute_path_books.csv' на фактические абсолютные пути к вашим файлам CSV
absolute_path_users = 'absolute_path_users.csv'
absolute_path_books = 'absolute_path_books.csv'

# Загрузим пользователей из файла users.csv
users = []
with open(absolute_path_users, 'r', newline='', encoding='utf-8') as user_file:
    user_reader = csv.reader(user_file)
    next(user_reader)  # Пропустим заголовок
    for row in user_reader:
        users.append(row[0])

# Создадим пустые массивы книг для каждого пользователя
user_books = {user: [] for user in users}

# Загрузим книги из файла books.csv и распределим их пользователям
with open(absolute_path_books, 'r', newline='', encoding='utf-8') as books_file:
    books_reader = csv.reader(books_file)
    next(books_reader)  # Пропустим заголовок
    for row in books_reader:
        book = {
            "Title": row[0],
            "Author": row[1],
            "Genre": row[2],
            "Pages": int(row[3]),
            "Publisher": row[4],
        }
        user_books[users[int(row[6])]].append(book)

# Теперь user_books содержит словарь, в котором ключи - это имена пользователей, а значения - их массивы книг
