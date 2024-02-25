"""
Задание №2 - "FuzzBuzz"
Напишите программу, которая перебирает последовательность от 1 до 100. Для чисел кратных 3 она должна написать:
"Fuzz" вместо печати числа, а для чисел кратных 5 печатать "Buzz". Для чисел которые кратны одновременно и 3 и 5 надо
печатать "FuzzBuzz". Иначе печатать число.
Последовательность от 1 до 100 можно создать с помощью range(1, 101)
"""
for values in range(1, 101):
    if values % 3 == 0 and values % 5 == 0:
        print("FuzzBuzz")
    elif values % 3 == 0:
        print("Fuzz")
    elif values % 5 == 0:
        print("Buzz")
    else:
        print(values)
