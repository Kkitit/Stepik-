import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
i = [x.split(': ') for x in lst_in]
d={}
for j in i:
    if j[0] not in d:
        d[j[0]] = {j[1]}
    d[j[0]].add(j[1])

