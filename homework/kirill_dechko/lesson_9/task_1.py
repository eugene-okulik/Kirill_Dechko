import datetime
"""Дана такая дата: "Jan 15, 2023 - 12:05:33"
Преобразуйте эту дату в питоновский формат, после этого:
1. Распечатайте полное название месяца из этой даты
2. Распечатайте дату в таком формате: "15.01.2023, 12:05"""
task_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(task_date, '%b %d, %Y - %H:%M:%S')
hum_month = python_date.strftime('%B')
hum_date2 = python_date.strftime('%d.%m.%Y, %H:%M')
print(hum_month)
print(hum_date2)
