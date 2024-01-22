# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
#
# Отсортируйте по убыванию значения количества повторяющихся слов.
#
# Пример
#
# На входе:
#
#
text = 'Hello world. Hello Python. Hello again.'
# На выходе:
#
#
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]


# import re
# from collections import Counter

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)

# # Другое решение
# text1 = 'Hello world. Hello Python. Hello again.'
# words = [] # список для слов
# word1 = '' # для составления слова
# for ch in text1.lower(): # бежим по символам
#     if ch.isalpha(): # если символ буква
#         word1 += ch # добавляем букву к слову
#     else:
#         if word1: # если слово, чтоб не считало пробелы
#             words.append(word1) # иначе к словарю добавляем слово
#         word1 = '' # слово обнуляем
# else:
#     if word1: # если слово, чтоб не считало пробелы
#         words.append(word1) # если предложение заканчивается яна букву, чтоб тоже добавлялось
#
# word_cnt = {(words.count(word1), word1) for word1 in set(words)}
# word_cnt = sorted(word_cnt, reverse=True)
# # print(word_cnt[:10]) # вывод в строку
# for i in range(len(word_cnt)):
#     print(f'{i+1}. {word_cnt[i][1]: <10} - {word_cnt[i][0]}')