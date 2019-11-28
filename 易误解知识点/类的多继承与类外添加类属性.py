class A(object):
    name = "A"


class B(object):
    name = "B"


class C(A, B):
    pass


print(C.name)
C.name = "C"
print(A.name)
print(B.name)
print(C.name)
