# list = [1, 2, 3, 5, 8, 15, 23, 38]

# def f(x):
#     return x**2
# newList = [(i, f(i)) for i in list if i % 2 == 0]
# print(newList)

# В файле хранятся числа, нужно выбрать четные и составить список пар (число, квадрат числа)
# Пример: [1, 2, 3, 5, 8, 15, 23, 38]
# Результат: [(2, 4), (8, 64), (38, 1444)]


# f = open('file.txt', 'r') 
# data = f.read() + ' '
# f.close()

# numbers = []
# while data != ' ':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]
# print(numbers)

# out = []
# for e in numbers:
#     if not e%2:
#         out.append((e, e**2))
# print(out)
#_________________

# упрощенный вариант

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x%2, res)
res = select(lambda x: (x, x**2), res)
print(res)

