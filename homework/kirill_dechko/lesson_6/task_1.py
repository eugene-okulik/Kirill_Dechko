"""
Задание №1
Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
“Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
dignissim vitae libero” и после этого выводит получившийся текст на экран. Знаки препинания не должны
оказаться внутри слова. Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова,
но уже преобразованного.
"""
text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
text_coll = text.split()
for word in text_coll:
    if word.endswith(","):
        find_len = len(word)
        word_list = list(word)
        find_val = word_list.pop(-1)
        end_word = "".join(word_list) + "ing" + find_val
        print(end_word, end=" ")
    elif word.endswith("."):
        find_len = len(word)
        word_list = list(word)
        find_val_2 = word_list.pop(-1)
        end_word = "".join(word_list) + "ing" + find_val_2
        print(end_word, end=" ")
    else:
        print(word, end=" ")
