import csv
import os
import json
import pprint

project_directory = os.getcwd()
csv_file_path = 'data/books.csv'
json_file_path = 'data/users.json'

absolute_path_csv = os.path.join(project_directory, csv_file_path)
absolute_path_json = os.path.join(project_directory, csv_file_path)



with open(absolute_path_csv, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(type(csv_reader))
    for row in csv_reader:
        print(row)



with open(json_file_path, 'r', encoding='utf-8') as json_file:
    # Загружаем данные из файла
    data = json.load(json_file)

    # Теперь переменная 'data' содержит данные из файла JSON
    pprint.pprint(data)