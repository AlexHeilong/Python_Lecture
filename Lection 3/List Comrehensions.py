# Данный лист нужен чтобы быстро создавать списки
from typing import Iterable


# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# list = []

# for i in range(1, 101):
#     # if i % 2 == 0:
#         list.append(i)
# print(list)

# Тот же самый список, но другим способом:
list = [i for i in range(1, 21) if i % 2 == 0]
print(list)

# если добавить пары кортежей
list = [(i, i) for i in range(1, 21) if i % 2 == 0]
print(list)

# с добавлением функции
def f(x):
    return x**3
list = [f(i) for i in range(1, 21) if i % 2 == 0]
print(list)

# та же функция, но в кортеже (пара: число и его куб)
def f(x):
    return x**3
list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(list)

