# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

natural_number = int(input('Введите число N: '))

def prime_factor(natural_number):
    l1 = list()
    divider = 2
    while (divider <= natural_number):
        if (natural_number % divider) == 0:
            l1.append(divider)
            natural_number = natural_number / divider
        else:
            divider += 1
    print(l1)

prime_factor(natural_number)