# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
#
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.
#
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
#
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
#
# Пример
#
# На входе:
#
#
# items = {
#     "ключи": 0.1,
#     "кошелек": 1.2,
#     "телефон": 1.5,
#     "зажигалка": 0.1
# }
# max_weight = 4.0
# На выходе, например, один из допустимых вариантов может быть таким:
#
#
# {'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}
# 1-variant
import itertools
from decimal import Decimal

# items = {
#     "ключи": 0.1,
#     "кошелек": 1.2,
#     "телефон": 1.5,
#     "зажигалка": 0.1,
#     "фонарь": 1.8,
#     "спички": 0.1,
#     "котелок": 2.8,
#     "топор": 2.2
# }
# max_weight = 3.4
# backpack = {}
#
# for item, weight in items.items():
#     max_weight -= weight
#     if max_weight > 0:
#         backpack.setdefault(item, weight)
#     else:
#         break
#     print(backpack)
#     print(max_weight)

# 2-variant
from decimal import Decimal

items = {
    "ключи": 0.1,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1,
    "фонарь": 0.8,
    "спички": 0.1,
    "котелок": 2.8,
    "топор": 2.2
}
max_weight = 3.4

max_weight_items = Decimal(str(max_weight))
backpack = {}
for i in items:
    if max_weight_items >= Decimal(str(items[i])):
        if i not in backpack:
            backpack.setdefault(i, items[i])
        max_weight_items -= Decimal(str(items.get(i)))
    else:
        continue
print(backpack)
