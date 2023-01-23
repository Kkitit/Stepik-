import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}

for i in lst_in:
    key, value = i.split()
    d[key] = d.get(key, []) + [value]

for key, value in d.items():
    print(f'{key}: ', end='')
    print(*value, sep=', ')
