def sort_list(func):
    def wr(*args):
        return dict(zip(*func(*args)))
    return wr

@sort_list
def get_list(s1, s2):
    s1=list(map(str, s1.split()))
    s2=list(map(str, s2.split()))
    return s1,s2

s1, s2 = input(), input()
d = get_list(s1, s2)
print(*sorted(d.items()))




