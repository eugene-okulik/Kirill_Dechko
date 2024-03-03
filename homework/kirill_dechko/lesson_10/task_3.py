"""
Задание №3
Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
(числа и операция передаются в аргументы функции). Функция выглядит примерно так:
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif .....
Программа спрашивает у пользователя 2 числа (вне функции)
Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
если числа равны, то функция calc вызывается с операцией сложения этих чисел
если первое больше второго, то происходит вычитание второго из певрого
если второе больше первого - деление первого на второе
если одно из чисел отрицательное - умножение
"""
first = int(input("Enter your first num: "))
second = int(input("Enter your second num: "))


def decor_calc_fn(any_calc):  # в данном случае any_calc = calc, т.к. декоратор @dekor_calc_fn вызван над функцией
    # calc()
    def wrapper(*any_args):  # параметры переданы при вызове функции calc как кортеж
        if any_args[0] == any_args[1]:  # теперь обращаемся к элементам кортежа по их индексу
            result = any_calc(any_args[0], any_args[1], "+")  # используем полученные аргументы, результат присваиваем
            # переменной result
            print(result)  # выводим результат на печать
        elif any_args[0] < 0 or any_args[1] < 0:
            result = any_calc(any_args[0], any_args[1], "*")
            print(result, 2)
        elif any_args[0] > any_args[1]:
            result = any_calc(any_args[0], any_args[1], "-")
            print(result)
        elif any_args[0] < any_args[1]:
            result = any_calc(any_args[0], any_args[1], "/")
            print(round(result, 3))
    return wrapper


@decor_calc_fn
def calc(first_fn, second_fn, operation):
    if operation == "+":
        sum_of_arg = first_fn + second_fn
        return sum_of_arg
    elif operation == "-":
        min_of_arg = first_fn - second_fn
        return min_of_arg
    elif operation == "*":
        mult_of_arg = first_fn * second_fn
        return mult_of_arg
    elif operation == "/":
        divs_of_arg = first_fn / second_fn
        return divs_of_arg


calc(first, second,)
