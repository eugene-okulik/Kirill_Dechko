INSERT INTO `groups` (title, start_date, end_date) values ('QA_Automation2', 'feb 2024', 'may 2024')  # создаем группу

select * from `groups` where title = 'QA_Automation2'  # проверка

INSERT INTO students (name, second_name, group_id) values ('Kirill2', 'Dechko2', 456)  # создаем студента

select * from students where group_id = 456 # проверяем

INSERT INTO books  (title, taken_by_student_id) values ('Book21', 503), ('Book21', 503)  # создали книги, записали на студента

select * from books b  where taken_by_student_id  = 503  # проверяем

INSERT INTO subjets (title) values ('SubjectDKA1'), ('SubjectDKA2')  # создаем предметы

select * from subjets s  where title = 'SubjectDKA1' or 'SubjectDKA2'  # проверяем

INSERT INTO lessons (subject_id, title) values (613, 'Lesson_1_SubjectDKA1'),
(613, 'Lesson_2_SubjectDKA1'), (614, 'Lesson_1_SubjectDKA2'), (614, 'Lesson_2_SubjectDKA2')  # создаем уроки
 
select * from lessons where subject_id IN (613, 614)  # проверяем

INSERT INTO marks (value, lesson_id, student_id)  # ставим оценки
values (100, 739, 503), (100, 740, 503), (50, 741, 503), (50, 742, 503)


select * from marks m  where student_id = 503  # проверяем

select value from marks  where student_id = 503  # получаем оценки студента

SELECT * FROM books b WHERE taken_by_student_id = 503 # книги на студента

SELECT * FROM students
JOIN `groups` ON students.group_id = groups.id
JOIN books ON students.id = books.taken_by_student_id
JOIN marks ON students.id = marks.student_id
JOIN lessons on marks.lesson_id  = lessons.id 
JOIN subjets on lessons.subject_id = subjets.id
where students.id = 503

# на всякий случай и так
SELECT `groups`.title, books.title, marks.value, lessons.title, subjets.title  FROM students
JOIN `groups` ON students.group_id = groups.id
JOIN books ON students.id = books.taken_by_student_id
JOIN marks ON students.id = marks.student_id
JOIN lessons on marks.lesson_id  = lessons.id 
JOIN subjets on lessons.subject_id = subjets.id
where students.id = 503
order by value DESC 