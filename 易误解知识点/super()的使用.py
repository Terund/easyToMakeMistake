class A(object):
    def show(self):
        print("base show")


class B(A):
    def show(self):
        print("drived show")


obj = B()
super(B, obj).show()
obj.show()
A().show()
