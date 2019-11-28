class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print("init")

    def mydefault(self):
        print("default")

    def __getattr__(self, name):
        return self.mydefault


a1 = A(10, 20)
a1.fn1()
a1.fn2()
a1.fn3()
