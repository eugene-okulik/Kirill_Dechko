"""Нужно сделать всё то же самое, но уже способ - на ваше усмотрение (можно с помощью срезов и метода index,
а можно с помощью split ). Получите из каждой строки с результатом число, прибавьте к полученному числу 10,
результат сложения распечатайте. Главное отличие - выполните всё с использованием функций. Нужно сделать так,
чтобы строк кода стало как можно меньше, и не было повторений одного и того же."""
result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"


def find_ind(result):
    index = int(result.index(":") + 1)
    index2 = int(result[index:])
    index2 += 10
    return index2


def find_ind2(result):
    one = result.split()
    one2 = int(one[-1]) + 10
    return one2


print(f"Вариант с index():\n{find_ind(result_1)}\n{find_ind(result_2)}\n{find_ind(result_3)}")
print(f"Вариант с split():\n{find_ind2(result_1)}\n{find_ind2(result_2)}\n{find_ind2(result_3)}")
