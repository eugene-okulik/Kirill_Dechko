# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
# print(name, last_name, city, phone, country)

# Задание 2
result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"
result_1_1 = int(result_1[-2:])
result_1_1 += 10
print(result_1_1)
result_1_2 = int(result_2[-3:])
result_1_2 += 10
print(result_1_2)
result_1_3 = int(result_3[-1:])
result_1_3 += 10
print(result_1_3)

# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
new_students = ", ".join(students)
subjects = ['math', 'biology', 'geography']
new_subjects = ", ".join(subjects)
my_text = f"Students {new_students} study these subjects: {new_subjects}"
print(my_text)

