d = {}
n = int(input())
while n != 0:
    if n not in d:
        d[n] = round(n ** 0.5, 2)
        print(d[n])
    else:
        print('значение из кэша:', d[n])
    n = int(input())