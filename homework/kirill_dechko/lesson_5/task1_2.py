# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
# print(name, last_name, city, phone, country)

# Задание 2
'''
Можно решать для каждой переменной отдельно:
ind2 = int(result_1.index(":") + 1)
result_1_11 = int(result_1[ind2:])
result_1_11 += 10
print(result_1_11)
но проще создать функцию
'''
result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"


def find_ind(result):
    index = int(result.index(":") + 1)
    index2 = int(result[index:])
    index2 += 10
    return index2


print(find_ind(result_1))
print(find_ind(result_2))
print(find_ind(result_3))


# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
new_students = ", ".join(students)
subjects = ['math', 'biology', 'geography']
new_subjects = ", ".join(subjects)
my_text = f"Students {new_students} study these subjects: {new_subjects}"
print(my_text)
