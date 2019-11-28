class A(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print("a=", self.__a, "b=", self.__b)

    def __call__(self, c):
        print("c=", c)


a1 = A(10, 20)
a1.myprint()
a1(80)
