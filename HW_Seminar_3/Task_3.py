# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

l1 = [1.1, 1.2, 3.1, 5, 10.01]
print(l1)
mx = l1[0]%1
mn = l1[0]%1
print(mn)
print(mx)
for i in range(1, len(l1)):
    if l1[i]%1>mx:
        mx = round(l1[i]%1, 2)
    if l1[i]%1>0 and l1[i]%1<mn:
        mn = round(l1[i]%1, 2)
print(mn)
print(mx)
print('-'*5)
print(f'min {mn}, max {mx}, max-min {round(mx-mn, 3)}')