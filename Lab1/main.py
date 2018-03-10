import random
import math


def pow(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number


def Ferma(A, k):
    for i in range(k):
        x = random.randint(2, A - 1)
        if math.gcd(A, x) != 1:
            return False
        if pow(x, A - 1, A) != 1:
            return False
    return True


k = 50
i = 0
while True:
    A = random.randint(2**100, 2**101)
    if Ferma(A, k):
        print('Вероятность того что число:' + A.__str__() + ' простое, равна: ' + (1 - (1/2)**k).__str__())
        print('Номер проверки: ' + i.__str__())
    i += 1