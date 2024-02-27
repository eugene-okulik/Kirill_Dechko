import random
"""Задание 1
Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool. 
Спросите у пользователя salary. А bonus пусть назначается рандомом.
Если bonus - true, то к salary должен быть добавлен рандомный бонус.
Примеры результатов:
10000, True - '$10255'
25000, False - '$25000'
600, True - '$3785'"""


salary = int(input("Enter your salary: "))
rand_bonus = [True, False]
bonus = (random.choice(rand_bonus))  # choice() выбор рандомного значения из списка
bonus_true = random.randint(1, 10000)
if bonus:
    new_salary = bonus_true + salary
    print(f"{salary}, {bonus} - '${new_salary}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
