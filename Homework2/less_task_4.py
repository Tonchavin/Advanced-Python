import math
import decimal

if __name__ == '__main__':
    deameter = float(input("Vvedite deameter: "))
    decimal.getcontext().prec = 48

    radius = decimal.Decimal(deameter / 2)
    PI = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
    area = PI * radius ** 2
    lenght = 2 * PI * radius

    print(f"{radius}\n{lenght}\n{area}")
