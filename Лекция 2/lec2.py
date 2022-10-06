## Файлы
# Как работать с файлами:
# Связать фаловую переменную с файлом,
# определив модификатор работы
# Режимы:
# a - открытие для добавления данных (на первоначальном этапе - создание файла)
# r - отурытие для чтения данных
# w - открытие для записи данных, а также создавать файлы 
# w+, r+ 

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # data - файловая переменная  = 'file.txt' - путь, 'a' - mode (режим)
# #data.writelines(colors) # разделителей не будет (функционал для записи данных)
# data.write('\nLINE 12\n')
# data.write('LINE 13\n')
# data.close() # разорвать подключение с файлом на диске - во избежании утечек памяти 

# with open('file.txt', 'a') as data: # данный вариант с автоматическим закрытием
#     data.write('LINE 2\n')
#     data.write('LINE 3\n')


#exit() - # функция, которая помогает не выполнять код ниже

## Чтение файла

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
#_______________________

## Функции и модули

# import hello # импорт функции из другого файла
# print(hello.f(1))

# import hello as h # импорт функции с установкой альяса
# print(h.f(2.3))
# ________________

# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required

# # в данном случае необходимо указать оба аргумента
# _____________________

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

# # в данном случае второй аргумент идет по умолчанию
# _________________________

# ## Возможность передачи неограниченного количества аргументов

# def concatenatio(*params): # для описания функции с множеством параметров ставится *
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', 2)) # a1d2
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...
# ___________________

# ## РЕКУРСИЯ - функция, вызывающая сама себя

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(e)
# print(list) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# ______________

## КОРТЕЖИ - это неизменяемый "список"

# a, b = 3, 4 # обычное множественное присваивание
# (a) = (3, 4, 41, 5) # кортеж
# print(a)
# print(a[0])
# print(a[-1])
# print(a[-2])



# t = ()
# print(type(t)) # tuple

# t = (1, )
# print(type(t)) # tuple

# t = (1)
# print(type(t)) # int

# t = (28, 9, 1990)
# print(type(t)) # tuple

# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']

# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) #  red
# print(t[2]) #  blue
# #print(t[10]) #  IndexError: tuple index out of range
# print(t[-2]) #  green
# #print(t[-200]) #  IndexError: tuple index out of range

# for e in t:
#     print(e) # red  green blue

# a = (3, 4, 5)
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r: {} g: {} b: {}'.format(red, green, blue))
# # r: red g: green b: blue
#__________________________

## Словари - неупорядоченные колекции с доступом по ключу

# Варианты написания словарей:
# dictionary = {}

# dictionary = \
#     {
#         'up' : '|',
#         'left' : '<-',
#         'right' : '->' # right - ключ, а -> - это значение
#     }
# print(dictionary) # {'up': '|', 'left': '<-', 'right': '->'}
# print(dictionary['left']) # <-

# for k in dictionary.keys(): 
#     print(k)  # просмотр ключей: up left right

# for k in dictionary.values(): 
#     print(k)  # просмотр значений: | <- ->

# print(dictionary['up'])

#______________________

## Множества 

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# print(type(colors))
# colors.add('red') # добавление имеющегося элемента - ничего не произойдет
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue', 'gray'}
# colors.remove('red')
# print(colors) # { 'green', 'blue', 'gray'}
# #colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # { 'green', 'blue', 'gray'}
# colors.clear()
# print(colors) #

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2 , 5}
# dl = a.difference(b) # dl = {1, 3}
# dl = b.difference(a) # dl = {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b)) # {1, 21, 3, 13} - изменяемые множества

# s = frozenset(a)  # неизменяемые (замороженные) множества
# _____________________________________________


## СПИСКИ

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)
# print()

# list1[0] = 123 # в результате замена будет в обоих списках
# list2[1] = 333 # в результате замена будет в обоих списках
# for e in list2:
#     print(e)
# print()

# for e in list1:
#     print(e)
# print()

# for e in list2:
#     print(e)
# print()
#__________

# удаление  элемента из списка

# list1 = [1, 2, 3, 4, 5]
# print(list1)
# print(list1.pop())  # последнего элемента
# print(list1)
# print(list1.pop(2)) # под индексом 2 (3)
# print(list1)
# print(list1.pop()) 
# print(list1)

# по аналогии вставляем элементы

list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1.append(6))
print(list1)
print(list1.insert(2, 11))
print(list1)

