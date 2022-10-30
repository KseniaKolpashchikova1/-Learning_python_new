# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint

l_1 = []
l_2 = []
random_num = int(input('Введите размер списка: '))
for i in range(random_num):
    l_1.append(randint(1, 10))
print(l_1)
for i in range((len(l_1)+1)//2):
    print(f'{l_1[i]} * {l_1[0-1-i]}')
    c = l_1[i] * l_1[0-1-i]
    l_2.append(c)
print(l_2)

