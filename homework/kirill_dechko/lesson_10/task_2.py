"""
Задание №2
Создайте универсальный декоратор, который будет управлять тем,
сколько раз запускается декорируемая функция
"""


def my_decorate_fn(any_fn, count=2):
    def wrapper():
        for _ in range(count):  # for i in range(count)- i заменил на _
            print(any_fn())
    return wrapper


@my_decorate_fn
def original_fn():
    text = "print me"
    return text


original_fn()
