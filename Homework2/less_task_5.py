if __name__ == '__main__':
    a = 1
    b = -5
    c = 6

    d = b ** 2 - 4 * a * c
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(x1, x2)