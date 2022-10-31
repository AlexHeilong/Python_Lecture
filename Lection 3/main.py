
# def f(x):
#     x**2

# g = f
# print(f(1))
# print(g(1))
#__________
# def f(x):
#     return x**2
# g = f # на переменную g возложили полностью функции f и она хранит в себе ссылку на функцию
# # print(f(2))
# # print(type(f))
# # print(type(g))
# # print(f(4))
# # print(g(4))

# def calc(x):
#     return x+10
# #print(calc(10))

# def calc2(x):
#     return x*10
# #print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc, 10)
#____________

# def sum(x, y):
#     return x + y

# sum = lambda x, y: x+y # переписал функцию выше

def mult(x, y):
    return x * y

def calc(op, a, b):
    #return op(a,b)
    print(op(a,b))

calc(mult, 4, 5)
calc(lambda x, y: x+y, 4, 5)