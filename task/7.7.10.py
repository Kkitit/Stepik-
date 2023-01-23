lst = [int(i) for i in input().split()]


def m_l(a, b):
    c = []
    n = len(a)
    R = len(b)
    i = j = 0

    while i < n and j < R:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


def is_is(a):
    s = len(a) // 2
    a1 = a[s:]
    a2 = a[:s]
    if len(a1) > 1:
        a1 = is_is(a1)
    if len(a2) > 1:
        a2 = is_is(a2)

    return m_l(a1, a2)


print(*is_is(lst))




