# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif.
# Откажитесь от магических чисел.
# Обязательно учтите год ввода Григорианского календаря.
# В коде должны быть один input и один print.

STANDARD_YEAR = 4
MIDDLE_YEAR = 100
HIGH_YEAR = 400

year = int(input('Введите год: '))

if (year % STANDARD_YEAR == 0
        and year % MIDDLE_YEAR != 0
        or year % HIGH_YEAR == 0):
    result = 'Год високосный: Да'
else:
    result = 'Год високосный: Нет'

print(result)
