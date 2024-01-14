#   Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
#   Используйте while и if. Попробуйте разные значения e и n.

# First variant
# n = int(input())
# e = int(input())
# summa = 0
#
# for i in range(1, n + 1):
#     if (i % 2 == 0) and (i % e != 0):
#         summa += i
# print(summa)

# Two variant
n, e = int(input()), int(input())
summa = 0

for i in range(2, n + 1, 2):
    if i % e != 0:
        summa += i
print(summa)
