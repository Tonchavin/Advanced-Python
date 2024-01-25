# У вас есть банковская карта с начальным балансом равным 0 у.е.
# Вы хотите управлять этой картой, выполняя следующие операции,
# для выполнения которых необходимо написать следующие функции:
#
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
#
# Пополнение счета:
#
# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
# Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
#
# Снятие средств:
#
# Функция withdraw(amount) позволяет клиенту снимать средства со счета.
# Сумма снятия также должна быть кратной MULTIPLICITY.
# При снятии средств начисляется комиссия в процентах от снимаемой суммы,
# которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.
#
# Завершение работы:
#
# Функция exit() завершает работу с банковским счетом. Перед завершением,
# если на счету больше RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.
#
# Проверка кратности суммы:
#
# Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
# Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.
#
# Пример
#
# На входе:
#
#
# deposit(10000)
# withdraw(4000)
# exit()
#
# print(operations)

# На выходе:
#
# ['Пополнение карты на 10000 у.е. Итого 10000 у.е.',
#  'Снятие с карты 4000 у.е. Процент за снятие 60 у.е.. Итого 5940 у.е.']

# 1-variant
import decimal
import random

MULTIPLICITY = 50  # ✔
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)  # ✔
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


# Введите ваше решение ниже
def check_multiplicity(amount):
    if amount % MULTIPLICITY != 0:
        print('Сумма должна быть кратной 50 у.е.')
    else:
        return True


def deposit(amount):
    global bank_account
    if check_multiplicity(amount):
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    else:
        print('Сумма должна быть кратной 50 у.е.')


def withdraw(amount: decimal) -> decimal:
    global bank_account
    if amount * PERCENT_REMOVAL > MAX_REMOVAL:
        temp_percent_removal = MAX_REMOVAL
    elif amount * PERCENT_REMOVAL < MIN_REMOVAL:
        temp_percent_removal = MIN_REMOVAL
    else:
        temp_percent_removal = amount * PERCENT_REMOVAL
    if bank_account >= (amount + temp_percent_removal):
        if check_multiplicity(amount):
            bank_account -= amount + temp_percent_removal
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {temp_percent_removal // 1} у.е.. '
                              f'Итого {bank_account // 1} у.е.')
    else:
        operations.append(f'Недостаточно средств. Сумма с комиссией {(amount + temp_percent_removal) // 1} у.е. На карте '
                          f'{bank_account} у.е.')


def exit():
    global bank_account
    if bank_account > RICHNESS_SUM:
        temp_rich_percent = bank_account * RICHNESS_PERCENT
        bank_account -= bank_account * RICHNESS_PERCENT
        operations.append(f'Вычтен налог на богатство 0.1% в сумме {temp_rich_percent} у.е. '
                          f'Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')


deposit(100000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)

# 2-variant
# import decimal
#
# MULTIPLICITY = 50  # ✔
# PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)  # ✔
# MIN_REMOVAL = decimal.Decimal(30)
# MAX_REMOVAL = decimal.Decimal(600)
# PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
# COUNTER4PERCENTAGES = 3
# RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
# RICHNESS_SUM = decimal.Decimal(10_000_000)
#
# bank_account = decimal.Decimal(0)
# count = 0
# operations = []
#
#
# def bank_card(*args):
#     print_mains()
#
#     global bank_account
#     global count
#     while True:
#         try:
#             count = int(input("Введите номер операции: "))
#         except ValueError:
#             continue
#
#         if count == 1:
#             amount = decimal.Decimal(int(input("Введите сумму депозита: ")))
#             operations.append(count)
#             if check_multiplicity(amount) == True:
#                 deposit(amount)
#         elif count == 2:
#             amount = decimal.Decimal(int(input("Введите сумму для снятия: ")))
#             operations.append(count)
#             if check_multiplicity(amount) == True:
#                 withdraw(amount)
#         else:
#             operations.append(count)
#             print_operations(operations)
#             exit()
#             break
#
#
# def print_mains():
#     print(""
#           "Выберите нужную операцию\n\n"
#           "1: Пополнение карты.\n"
#           "2: Снятие с карты.\n"
#           "3: Выход.\n")
#
#
# def print_operations(operations):
#     global bank_account
#     n = 1
#     print("\nВСЕ ОПЕРАЦИИ ПО СЧЕТУ:\n")
#     for i in operations:
#         if i == 1:
#             print(f"{n} операция = Операция внесения наличных.")
#             n += 1
#         elif i == 2:
#             print(f"{n} операция = Операция снятия наличных.")
#             n += 1
#     print(f"Наличных на счету: {bank_account}")
#
#
# def check_multiplicity(amount):
#     if amount % MULTIPLICITY != 0:
#         print('Сумма должна быть кратной 50 у.е.')
#     else:
#         return True
#
#
# def deposit(amount):
#     global bank_account
#     bank_account += amount
#     print(f"Пополнение карты на {amount} у.е. Итого {bank_account} у.е.")
#     return bank_account
#
#
# def withdraw(amount):
#     global bank_account
#     prosent = amount * PERCENT_REMOVAL
#     result = 0
#     if (bank_account > amount + prosent and
#             bank_account > amount + MIN_REMOVAL and
#             bank_account > amount + MAX_REMOVAL):
#         if MIN_REMOVAL <= amount <= MAX_REMOVAL:
#             result = amount + amount
#             bank_account -= amount + amount
#         else:
#             result = amount + prosent
#             bank_account -= amount + prosent
#     else:
#         print("Недостаточно наличных")
#     print(f'Снятие с карты {amount} у.е. Процент за снятие {result} у.е.. Итого {bank_account} у.е.')
#     return bank_account
#
#
# def exit():
#     global bank_account
#
#     if bank_account > RICHNESS_SUM:
#         bank_account = bank_account - (bank_account * RICHNESS_PERCENT)
#         print(f"Наличных на счету: {bank_account} снятые проценты за роскошь: {bank_account * RICHNESS_PERCENT}")
#
#
# bank_card()
