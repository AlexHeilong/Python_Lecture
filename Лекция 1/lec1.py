# from tokenize import cookie_re
# from xmlrpc.client import boolean


# print('Hello World')

# типы данных и переменная
# int, float, boolean, str, list, None

# value = None
# print(type(value))

# print(type(a))
# print(type(b))
# value = 1234
# print(type(value))

# a = 123
# b = 12.3
# s = 'hello \nworld' # вывод строки
# print(s)
# print(a, b, s)
# print(a, '-',b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', '3']
# col = ['Hello, World', 1, 2, 3.5, True]
# print(list)
# print(col)
#__________________________

# Ввод и вывод данных

# print() - вывод данных
# input() - ввод данных

# print('Введите a: ')
# a = input()
# print('Введите b: ')
# b = input()
# # print(a, b)
# # print('{} {} '.format(a, b))
# # print(f'{a} {b}')
# print(a, '+', b, '=', a+b )
#_____________________________

# Арифметические операции
# a = 2
# b = 8
# c = a-b
# print(c) # обычные арифметические операции

# a = 12
# b = 8
# c = a / b # обычное деление и получение вещественного числа (1.5)
# print(c)

# a = 12
# b = 8
# c = a // b # деление и получение целочисленного числа (1)
# print(c)

# a = 12
# b = 8
# c = a % b # получить остаток от деления (4)
# print(c)

# a = 12
# b = 8
# c = a ** b # возведение в степень (429981696)
# print(c)

# a = 1.3
# b = 3
# c = round(a * b) # округление полученного числа (без аргументов) (4)
# print(c)

# a = 1.312312
# b = 3
# c = round(a * b, 5) # округление полученного числа 
# # (с аргументом до 5 знаков после запятой) (3.93694)
# print(c)


# # сокращенные операции присваивания
# a = 3
# a = a + 5
# # print(a)
# _________________________________

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# Кое-что еще: is, is not, in, not in

# a = 1 > 4
# print(a) # False

# a = 1 < 4 and 5 > 2
# print(a) # True

# a = 1 == 4
# print(a) # False

# a = 1 != 4
# print(a) # True

# a = 'qwe'
# b = 'qwe'
# print(a == b) # True

# a = [1, 2]
# b = [1, 2]
# print(a == b) # True

# a = 1 < 3 < 5 < 10
# print(a) # True

# func = 1
# T = 4
# x = 2
# print(func<T>(x)) # True

# f = 1 > 2 or 4 < 6
# print(f) # True - дизюнкция двух высказываний называетя истинным, 
# # когда хотя бы одно из высказываний - истина

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f) # True - 2 присутствует в списке

# f = [1, 2, 3, 4]
# print(f)
# print(6 in f) # False - 6 отсутствует в списке

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f) # False - условие неверно

# is_odd = f[0] % 2 == 0
# print(is_odd) # False - f[0] - элемент равен 1, 
# # поэтому остаток при делении на 2 не может быть равен 0

# is_odd = not f[0] % 2
# print(is_odd) # False - f[0] - другой вариант записи варианта выше

# _____________________________________

# Управляющие конструкции: if, if-else
# from re import M
# from tkinter import N


# if condition:
#     operator 1
#     operator 2
#     ...
#     operator n
# else 
#     operator n + 1
#     operator n + 2
#     ...
#     operator n + m

# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# else:
#     print(b)

#_________

# if condition1:
#      operator 
# elif condition2:
#      operator 
# elif condition3:
#      operator 
# else:
#     operator

# userName = input('Введите ваше имя: ')
# if userName == 'Маша':
#     print('Ура, это же Маша!!!')
# elif userName == 'Марина':
#     print('Я так ждал Вас, Марина!!!')
# elif userName == 'Ильнар':
#     print('Ильнар - ТОП!!!')
# else:
#     print('Привет, ', userName, '!!!' )
#_____________________________

# Циклы:
# while - цикл позволяет выполнить блок операторов какое-то количество раз

# while condition:
#     operator 1
#     operator 2
#     ...
#     operator n

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)
# ____________

# while-else: выполняется в том случае, когда основное тело цикла перестает работать

# while condition:
#     operator 1
#     operator 2
#     ...
#     operator n
# else 
#     operator n + 1
#     operator n + 2
#     ...
#     operator n + m

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит))')
# print(inverted)
# __________________________

# Цикл for - когда мы занем, что хотим
# for i in enumeration:
#     operator 1
#     operator 2
#     ...
#     operator n

# for i  in 1, 2, 3, 4:
#     print(i**2)
# print(' ')    


# list = [1, 2, 3, 4]
# for i  in 1, 2, 3, 10, 4:
#     print(i)
# print(' ') 

# r = range(10)
# for i in r:
#     print(i)
# print(' ')     

# for i in range(5):
#     print(i)
# print(' ') 

# for i in range(1, 10, 2): # диапозон от 1 до 10(9) с шагом +2
#     print(i)
# print(' ') # 1 3 5 7 9 
# __________________________

# Немного о строках:

# text = 'съешь еще этих мягких французких булок'
# print(len(text))                    # 39
# print('еще' in text)                # True
# print(text.isdigit())               # False
# print(text.islower())               # True
# print(text.replace('еще', 'ЕЩЁ'))
# for c in text:
#     print(c)

# print(text[0])  # c
# print(text[1])  # ъ
# ——————————————————————————————————————————————————————

## Списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(len(numbers))
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)
#____________

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue

# for e in colors:
#     print(e*2) # redred greengreen blueblue

# colors.append('gray') # добавить элемент в конец
# print(colors) # ['red', 'green', 'blue', 'gray']
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #  удаление элемента по названию (значению)
# print(colors) # ['green', 'blue', 'gray']
# del colors[0] # удаление элемента по индексу 
# print(colors) # ['blue', 'gray']
# _______________________________________

## Функции

# Это фрагмент программы, используемый многократно

# def function_name(x): # def + имя функции + (аргументы)
#     body_line 1
#     ...
#     body_line n
#     optional return

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 2.3
print(f(arg))
print(type(f(arg)))
