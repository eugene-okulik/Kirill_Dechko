"""
Задание №2
Создайте универсальный декоратор, который будет управлять тем,
сколько раз запускается декорируемая функция
"""


def my_decorate_fn(any_fn, count=2):
    def wrapper():
        my_count = 0
        for _ in range(count):  # for i in range(count)- i заменил на _
            while my_count < count:
                print(any_fn())
                my_count += 1
    return wrapper


@my_decorate_fn
def original_fn():
    text = "print me"
    return text


original_fn()
