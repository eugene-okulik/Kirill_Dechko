"""
Задание №1
Создайте универсальный декоратор, который можно будет применить к
любой функции. Декоратор должен делать следующее: он должен
распечатывать слово "finished"после выполнения декорированной функции.
"""


def my_finish_decor(original_func):
    def wrapper():
        original_func()
        print("finished")
    return wrapper


@my_finish_decor
def any_func():
    text = "print me"
    print(text)


any_func()
