"""Задание 2.
Напишите функцию-генератор, которая генерирует список чисел фибоначчи
Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число"""


def my_fib(x):
    a = 0
    b = 1
    my_count = 1
    while my_count <= x:
        yield b
        my_c = a + b
        a = b
        b = my_c
        my_count += 1


count = 1
found_fib_num = []
for c in my_fib(100000):
    if count + 1 in [5, 200, 1_000, 100_000]:
        found_fib_num.append(c)
        print(found_fib_num[-1])
    count += 1

