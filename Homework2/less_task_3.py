number = 10
result = ""

while number != 0:
    result = str(number % 2) + result
    number //= 2

# while number != 0:
#     result = str(number % 8) + result
#     number //= 8

print(result)

print(bin(10))
print(oct(12))
