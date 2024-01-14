list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

count = 0

for num1 in list1:
    if num1 in list2:
        count += 1

print(f"Количество совпадающих чисел: {count}")

