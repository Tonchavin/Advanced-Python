num = 2

if not 1 < num <= 100000:
    print("Число должно быть больше 1 и меньше 100000")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Не является простым")
            break
    else:
        print("Простое")

