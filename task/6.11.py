import sys

z = list(map(str.strip, sys.stdin.readlines()))
d = {}
for i in z:
    if i not in d:
        d[i] = i
        print("HTML-страница для адреса", d[i])
    else:
        print("Взято из кэша: HTML-страница для адреса", d[i])