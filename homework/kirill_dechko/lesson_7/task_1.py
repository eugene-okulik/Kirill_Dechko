import random
"""Задание №1 - "Угадайка"
Создайте такую программу:
Программа хранит какую-либо цифру в переменной.
Программа просит пользователя угадать цифру. Пользователь вводит цифру.
Программа сравнивает цифру с той, что хранится в переменной.
Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
Т.е. программа не завершается пока пользователь не угадает цифру."""
rand_int = random.randint(0, 5)  # Ограничил диапазон до 5
while True:
    user_int = int(input("Пожалуйста, введите любое число от 0 до 5: "))
    if user_int != rand_int:
        print("Попробуйте снова")
        continue
    print("Поздравляю! Вы угадали")
    break