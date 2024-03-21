import csv
import mysql.connector as mysql  # импортируем модуль взаимодействия с mysql
import dotenv  # для работы с dotenv надо импортировать модуль dotenv
import os  # для работы с dotenv надо импортировать модуль os

dotenv.load_dotenv()  # если написать эту строку, то на время работы, если у нас есть файл .env все указанные в нем
# параметры будут записаны в системные переменные

db = mysql.connect(  # вводим данные для подключения к БД, для обращения к
    # данным сохраняем все в переменную
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

cursor.execute("select students.name, students.second_name, `groups`.title as 'group_title', "
               "books.title as 'book_title', subjets.title as 'subject_title',"  # в файле csv названия колонок
               # отличаются от названий в БД, поэтому таким запросом переименовываем названия полученные из БД
               # в нужные нам, которые будут совпадать с названиями колонок из csv
               " lessons.title as 'lesson_title', marks.value as 'mark_value' "
               "FROM students "
               "JOIN `groups` ON students.group_id = groups.id "
               "JOIN books ON students.id = books.taken_by_student_id "
               "JOIN marks ON students.id = marks.student_id "
               "JOIN lessons ON marks.lesson_id = lessons.id "
               "JOIN subjets ON lessons.subject_id = subjets.id "
               "ORDER BY value")
find_inf = cursor.fetchall()

file_path = r'C:\Kirill_Dechko\homework\eugene_okulik\Lesson_16\hw_data\data.csv'
finded_elem = []  # создаем пустой список
with open(file_path, newline='') as csv_file:  # берем данные из csv
    data_file = csv.reader(csv_file)  # записываем эти данные в переменную data_file
    for elem in data_file:  # читаем данные из переменной data_file
        finded_elem.append(elem)  # добавляем элементы в пустой список и получаем список списков


keys = finded_elem[0]  # указываем что названия ключей хранятся в строке с индексом 0 (верхняя строка)
my_dict = [dict(zip(keys, values)) for values in finded_elem[1:]]  # zip(keys, values) объединяет элементы из списка
# keys (список заголовков) с соответствующими элементами из списка values (список данных).
# for values in finded_elem[1:] означает, что мы проходимся по каждой строке данных в списке finded_elem,
# начиная со второй строки (первая строка была использована как заголовки).
# dict(...) создает словарь, используя пары ключ-значение из zip(keys, values)

for row in my_dict:  # проходим циклом по строкам my_dict
    if row not in find_inf:  # если строки нет в БД выводим ее на печать
        print(row)

db.close()
