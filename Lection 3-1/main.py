# Урок 3. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# Набор простых функций:
# 1)
# def sum(x):
#     return x + 10
# # 2)
# def sum1(x):
#     return x + 22
# # 3)
# def sum2(x):
#     return x + 242
# # 4)
# def mult(x):
#     return x**2
# # 5)
# def mult1(x):
#     return x**3
# # 6)
# def mult2(x):
#     return x**5
# __________________________

# def f(x):
#     x**2

# g = f # простое присвоение значения к переменной g
# print(f(1)) # - вывод функции
# print(g(1)) # - вывод функции - тот же результат
# print(type(f)) # - проверка на тип данных (функция)
# print(type(g)) # - проверка на тип данных (функция)

# !!!! Если функция может быть положена в какую-то переменную (g = f),
# то мы можем в качестве аргумента какой-то функции передать функцию:
# def f(x):
#     return x ** 2
#
# g = f # - переменная g принимает всю функцию, а не вызывает или фиксирует какое-то значение
#
# print(type(f)) # - проверка на тип данных (функция)
# print(type(g)) # - проверка на тип данных (функция)
# print(f(4))
# print(g(4)) # тот же функционал и значения
# # - т.е. в нашем коде теперь есть переменная, которая хранит ссылку на функцию
# ______________________________
# Зачем это может потребоваться? Рассмотрим следующий пример:

# def calc1(x):
#     return x+10
# #print(calc1(10)) #- нам нужна функция с +10
#
# def calc2(x):
#     return x*10
# #print(calc2(10)) # но вдруг нам понадобится потом функция с *10?
#
# # А затем нужно будет вычетание или деление и нам придется плодить функции с одинаковой логикой
# # В идеале нужно взять функцию "calc", которая в качестве аргумента будет примать операцию и что-то выдавать:
#
# def math(opertion, x): # создаем функцию, которая в качестве аргумента принимает функцию (operation) и значение
#     print(opertion(x))
# math(calc2, 10) # в качестве первого аргумента указываем название функции без ее вызова (), и вторым - значение
# math(calc2, 10) # таким образом, получется функция х*10 или 10*10 = 100
# math(calc1, 10) # х + 10 или 10 + 10 = 20
# ______________________________

# Теперь тоже самое, но с двумя аргументами, которые представляют собой отдельные функции:
# def sum(x, y):
#     return x+y
# f = sum # опять же в переменную f внесли всю функцию
# def mult(x, y):
#     return x*y
#
# def calc(op, a, b): # первый аргумент - функция (операция); второй и третий - это значения (x и y)
#     print(op(a, b))
#     #return op(a, b)
#
# calc(mult, 4, 5) # сработала функция перемножения = 20
# calc(f, 3, 7) # сработала функция сложения (при использовании переменной f) = 10
#______________________________________________

# Теперь сократим написание функции еще больше:
# Та же функция что и выше:
# def sum(x, y):
#     return x+y
# f = sum
#_________________________
# f = lambda q, w: q + w
#
# def calc(op, a, b):
#     print(op(a, b))
# calc(f, 3, 7)
#___________________________
#Следующим этапом убираем переменную (f) и сразу записываем в конечную функцию:
# def calc(op, a, b):
#     print(op(a, b))
# calc(lambda x, y: x + y, 3, 7)
# ____________________________



