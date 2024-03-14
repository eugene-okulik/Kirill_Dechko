import os
import datetime

bace_path = os.path.dirname(__file__)
file_path = os.path.join(bace_path, 'data.txt')
new_file_path = os.path.join(bace_path, 'data2.txt')
homework_path = os.path.dirname(os.path.dirname(bace_path))
o_lesson_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():  # Создаем генератор который обработает файл из директории o_lesson_path, по одной строке за проход
    with open(o_lesson_path, "r") as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():  # для переменной data_line (которую создал генератор) и записал туда строку
    with open(o_lesson_path, 'a'):  # переходим к переменной по пути o_lesson_path
        data_line = data_line.split(" - ")  # преобразовываем строку в список делим строку по " - "
        data_line.pop(-1)  # удаляем последний элемент списка (остается дата с индеском 1., 2., 3.)
        data_line = ' '.join(data_line)  # преобразовываем список в строку
        if data_line.startswith("1."):  # если строка насинается с 1.
            data_line = data_line[3:]  # оставляем в строке только дату
            date = datetime.datetime.strptime(data_line, '%Y-%m-%d %H:%M:%S.%f')  # преобраз. строку в дату
            new_date = date + datetime.timedelta(days=7)
            print(new_date)
        if data_line.startswith("2."):
            data_line = data_line[3:]
            date = datetime.datetime.strptime(data_line, '%Y-%m-%d %H:%M:%S.%f')
            weak_day = date.strftime('%d')
            print(weak_day)
        if data_line.startswith("3."):
            data_line = data_line[3:]
            date = datetime.datetime.strptime(data_line, '%Y-%m-%d %H:%M:%S.%f')
            now = datetime.datetime.now()
            differ_day = now - date
            print(differ_day)
