# Task. Создать файл со списком: [1, 2, 3, 5, 8, 15, 23, 38]. Нужно выбрать четные и составить список пар (число - квадрат)

#  Сперва по-старинке:

# #with open('file.txt', 'w') as f:
#     f.writelines('1, 2, 3, 5, 8, 15, 23, 38')

# with open("file.txt", "r") as f:
#     data = f.read().replace(',', ' ').split()
#     data_ints = [int(i) for i in data]
#     print(data_ints)
#
# out = []
# for e in data_ints:
#     if not e%2:
#         out.append((e, e**2))
# print(out)
# _________________________
# Теперь тоже самое, но по новой теме:

def select(f, col): # Далее мы создаем функцию, где аргументы: функция и данные
    return [f(x) for x in col]

def where(f, col): # Еще одна функция, которая принимает функцию и набор данных
    return [x for x in col if f(x)]
data = '1, 2, 3, 5, 8, 15, 23, 38'.replace(',', ' ').split()

result = select(int, data) # первым аргументом будет int - которая выступит в роли функции, которая преобразует строки в число - все так просто
print(result)
result1 = where(lambda x: x%2==0, result)
# result1 = where(lambda x: not x%2, result) - тоже самое
print(result1)
result2 = select(lambda x: (x, x**2), result1)
print(result2)


# numbers = []
#
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos: +1:]
# print(numbers)
#
# out = []
# for e in numbers:
#     if not e%2:
#         out.append((e, e**2))
# print(out)

# def select(f, col): # Далее мы создаем функцию, где аргументы: функция и данные
#     return [f(x) for x in col]
#
# def where(f, col): # Еще одна функция, которая принимает функцию и набор данных
#     return [x for x in col if f(x)]
# data = '1, 2, 3, 5, 8, 15, 23, 38'.split()
#
# result = select(int, data)
# print(result)







