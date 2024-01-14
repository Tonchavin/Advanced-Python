import fractions
#
# frac1 = "1/2"
# frac2 = "1/3"
#
# f1 = frac1.split("/")
# f1_0 = int(f1[0])
# f1_1 = int(f1[1])
#
# f2 = frac2.split("/")
# f2_0 = int(f2[0])
# f2_1 = int(f2[1])
#
# frac1 = fractions.Fraction(f1_0, f1_1)
# frac2 = fractions.Fraction(f2_0, f2_1)
#
# print(f"Сумма дробей: {frac1 + frac2}")
# print(f"Произведение дробей: {frac1 * frac2}")
# print(f"Сумма дробей: {frac1 + frac2}")
# print(f"Произведение дробей: {frac1 * frac2}")
from fractions import Fraction

frac1 = '1/2'
frac2 = '1/3'

# Разбиваем строки на числитель и знаменатель без использования map
numerator1_str, denominator1_str = frac1.split('/')
numerator2_str, denominator2_str = frac2.split('/')

# Преобразуем строки в целые числа
numerator1 = int(numerator1_str)
denominator1 = int(denominator1_str)
numerator2 = int(numerator2_str)
denominator2 = int(denominator2_str)

common_denominator = denominator1 * denominator2

new_numerator1 = numerator1 * denominator2
new_numerator2 = numerator2 * denominator1

summation_numerator = new_numerator1 + new_numerator2
multiplication_numerator = numerator1 * numerator2

print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")

# Преобразуем введенные строки в объекты Fraction
fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

# Вычисляем сумму и произведение дробей
summation = fraction1 + fraction2
multiplication = fraction1 * fraction2

print(f"Сумма дробей: {summation}")
print(f"Произведение дробей: {multiplication}")
