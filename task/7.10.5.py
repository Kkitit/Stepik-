def rr(tp="list"):
    def zam(s):
        if tp == "list":
            s = list(map(int, s.split()))
            return s
        else:
            s = tuple(map(int, s.split()))
            return s

    return zam


tp = input()
li = input()
print(rr(tp)(li))




