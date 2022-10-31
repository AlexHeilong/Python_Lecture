# Функция filter() - принимает указзаную функцию к каждому элементу итерируемого объекта
# и возвращает итератор  с теми объектами, для которых функция вернула True
# f(x) = x - четное
# filter(f, [1, 2, 3, 4, 5])
#           [   2,    4]
# Нельзя пройтись дважды

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data)) # x:x%2==0
# print(res)


# Доработанная задача из файла Task for compre... Удаляем функцию where

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)