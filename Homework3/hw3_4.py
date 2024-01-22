# Дан список повторяющихся элементов lst. Вернуть список с
# дублирующимися элементами. В результирующем списке не должно быть
# дубликатов.


# На выходе:
# [1, 2, 3]

lst = [1, 2, 3, 4, 4, 4]

duplicates = set()

for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)

result = list(duplicates)
print(result)
