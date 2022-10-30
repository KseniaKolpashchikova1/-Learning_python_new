# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n+1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))




# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n+1):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))




# f1 = 1
# f2 = 1
# numm_f = int(input('Введите число (не менее 2): '))
# print(f1, f2, end = ' ')
# for i in range(2, numm_f):
#     f1, f2 = f2, f1 + f2
#     print(f2, end = ' ')


# f1 = 1
# f2 = 1
# numm_f = int(input('Введите число (не менее 2): '))
# print(f1, f2, end = ' ')
# for i in range(2, numm_f):
#     f1, f2 = f2, f1 + f2
#     print(f2, end = ' ')

