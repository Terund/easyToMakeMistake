def f1(n):
    def inner(a):
        return n * a

    return inner


zw = f1(7)
print(zw(9))
