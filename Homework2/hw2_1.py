# num = 255
#
# print(f"Шестнадцатеричное представление числа: {hex(num).removeprefix('0x').upper()}")
# print(f"Проверка результата: {hex(num)}")
num = 255

HEX = 16
hex_digits = "0123456789ABCDEF"

hex_num = ""
test_hex_num = hex(num)

while num > 0:
    remainder = num % HEX
    hex_num = hex_digits[remainder] + hex_num
    num //= HEX

print("Шестнадцатеричное представление числа:", hex_num)
print("Проверка результата:", test_hex_num)

