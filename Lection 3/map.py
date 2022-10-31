# Функция map - применяет указанную фукцию к каждому элементу итерируемого объекта
# и возвращает итератор с новыми объектами
# f(x) => x + 10
# map(f, [1, 2, 3, 4, 5])
#        [11,12,13,14,15] 
# Нельзя пройтись дважды


# li = [x for x in range(1, 20)]
# print(li)
# li = list(map(lambda x:x+10, li))
# print(li)


# data = list(map(int, input('...: ').split()))
# print(data)


# data = map(int, '1 2 3'.split())

# for e in data:
#     print(e)

# print('---')

# for e in data:
#     print(e)

# Доработанная задача из файла Task for compre... Удаляем функцию select

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)