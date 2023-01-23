import sys

# 
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}

for i in lst_in:
    value, key = i.split()
    if key in d:
        d[key] += [value]
    else:
        d[key] = [value]

print(*sorted(d.items()))
