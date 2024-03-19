import mysql.connector as mysql  # импортируем модуль взаимодействия с mysql

db = mysql.connect(  # вводим данные для подключения к БД, для обращения к
    # данным сохраняем все в переменную
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# 1
req_ins_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(req_ins_group, ('DKA_Group2', 'feb- 22', 'may- 28'))  # здесь перечесляем values для %s, %s, %s
db.commit()
# Получение идентификатора последней вставленной строки
groups_id = cursor.lastrowid
# Запрос на получение данных из таблицы `groups` по идентификатору
cursor.execute("SELECT * FROM `groups` WHERE id = %s", (groups_id,))  # внимательно с запятыми и
# скобками
print(cursor.fetchall())

# 2
req_ins_student = "INSERT INTO students (name, second_name, group_id) values (%s, %s, %s)"
cursor.execute(req_ins_student, ('Kirill458', 'Dechko458', groups_id))
db.commit()
student_id = cursor.lastrowid
cursor.execute("SELECT * FROM students where id = %s", (groups_id,))
cursor.fetchall()

# 3
book_list = ['Book', 'Book1', 'Book2', 'Book3']
book_id = []  # создаем пустой список куда запишем id добавленных книг
for elem in book_list:
    req_ins_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
    cursor.execute(req_ins_books, (elem, student_id))
    db.commit()
    book_id.append(cursor.lastrowid)  # добавляем в список id созданной записи
    cursor.execute("select * from books where id = %s", (cursor.lastrowid,))
    print(cursor.fetchall())

# 4
sub_list = ['Subject_DKA1', 'Subject_DKA2']
subj_id = []
for elem in sub_list:
    rec_int_subj = "INSERT INTO subjets (title) VALUES (%s)"
    cursor.execute(rec_int_subj, (elem,))  # здесь перечесляем values для %s внимательно с запятыми и скобками
    #  особенно где добавляем одно значение
    db.commit()
    subj_id.append(cursor.lastrowid)
    cursor.execute("select * from subjets where id = %s", (cursor.lastrowid,))
    print(cursor.fetchall())

# 5
lessons_list = ['Lesson_1_SubjectDKA12', 'Lesson_2_SubjectDKA13', 'Lesson_3_SubjectDKA14', 'Lesson_4_SubjectDKA15']
lesson_id = []
for subj, lessons in zip(subj_id, [lessons_list[:2], lessons_list[2:]]):  # объединяем идентификаторы предметов с
    # соответствующими списками уроков
    for lesson in lessons:  # Добавляем уроки для каждого предмета
        req_ins_lessons = "INSERT INTO lessons (subject_id, title) VALUES (%s, %s)"
        # Предполагаем, что cursor.execute и db.commit() - это функции для работы с базой данных
        cursor.execute(req_ins_lessons, (subj, lesson))
        db.commit()
        lesson_id.append(cursor.lastrowid)
        cursor.execute("SELECT * FROM lessons WHERE id = %s", (cursor.lastrowid,))
        print(cursor.fetchall())

# 6
marks_list = [100, 50, 24, 34]
marks_id = []
for lesson, mark in zip(lesson_id, marks_list):
    req_ins_mark = "INSERT INTO marks (lesson_id, student_id, value) VALUES (%s, %s, %s)"
    cursor.execute(req_ins_mark, (lesson, student_id, mark))
    db.commit()
    marks_id.append(cursor.lastrowid)
    cursor.execute("SELECT * FROM marks WHERE id = %s", (cursor.lastrowid,))
    print(cursor.fetchall())

print(f"1. Group id: {groups_id}")
print(f"2. Student id: {student_id}")
print(f"3. Books ids: {book_id}")
print(f"4. Subjects ids: {subj_id}")
print(f"5. Lessons ids: {lesson_id}")
print(f"6. Marks ids: {marks_id}")

cursor.execute(f"SELECT `groups`.title, books.title, marks.value, lessons.title, subjets.title "
               f"FROM students "
               f"JOIN `groups` ON students.group_id = groups.id "
               f"JOIN books ON students.id = books.taken_by_student_id "
               f"JOIN marks ON students.id = marks.student_id "
               f"JOIN lessons ON marks.lesson_id = lessons.id "
               f"JOIN subjets ON lessons.subject_id = subjets.id "
               f"WHERE students.id = {student_id} ORDER BY value DESC")
print(cursor.fetchall())

db.close()
