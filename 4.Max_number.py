x = int(input('введите число: '))
xmax = 0
i = x

while i:
    if i % 10 > xmax:
        xmax = i % 10
    i //= 10
print('Максимальная цифра числа', x, ':', xmax)