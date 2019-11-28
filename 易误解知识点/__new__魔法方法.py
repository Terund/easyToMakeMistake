class B(object):
    def fn(self):
        print("B fn")

    def __init__(self):
        print("b init")


class A(object):
    def fn(self):
        print("A fn")

    def __new__(cls, a):
        print("new", a)
        if a > 10:
            return super(A, cls).__new__(cls)
        return B()

    def __init__(self, a):
        print("init", a)


a1 = A(5)
a1.fn()
a2 = A(20)
a2.fn()
