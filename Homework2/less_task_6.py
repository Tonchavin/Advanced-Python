if __name__ == '__main__':

    summa = 0
    count = 0
    LIMIT = 5000000
    MIN_LIMIT = 30
    MAX_LIMIT = 600
    PERSENT = 0.015

    while True:
        print(f"Сумма на счете: {summa}")
        print(f"1: Пополнить\n2: Снять\n3: Выйти")
        n = int(input("Выберите опцию: "))
        if summa > LIMIT:
            summa *= 0.9

        if n == 1 or n == 2:
            count += 1
            if count % 3 == 0:
                summa *= 1.03

        if n == 1:
            s = int(input("Введите сумму пополнения: "))
            if s % 50 == 0:
                summa += s
            else:
                print("Введите сумму кратное 50")
            continue

        if n == 2:
            s = int(input("Введите сумму для снятия: "))
            pr = max(min(s * PERSENT, MAX_LIMIT), MIN_LIMIT)
            if summa > s + pr:
                summa -= s + pr
                continue

        if n == 3:
            print(f"Сумма на счете: {summa}")
            break
