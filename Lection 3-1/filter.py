# Функция filter() - принимает указзаную функцию к каждому элементу итерируемого объекта
# и возвращает итератор  с теми объектами, для которых функция вернула True
# f(x) = x - четное
# filter(f, [1, 2, 3, 4, 5])
#           [   2,    4]
# Нельзя пройтись дважды

# data = [x for x in range(1, 10)]
# #result = list(filter(lambda x: x%2 == 0, data)) # в качесве аргумента входит lambda, проверяющая значения на четность
# result = list(filter(lambda x: not x% 2, data)) # тоже самое
# print(result)
# _____________________
# Теперь вновь вернемся к первоначальному примеру и заменим функцию where

data = '1, 2, 3, 5, 8, 15, 23, 38'.replace(',', ' ').split()

result = map(int, data) # вместо select сразу вписываем функцию "map", без дополнтельных условий
#result1 = list(filter(lambda x: x%2==0, result)) # заменили функцию where, без дополнтельных условий
result1 = list(filter(lambda x: not x%2, result))
print(result1)
result2 = list(map(lambda x: (x, x**2), result1))
print(result2)