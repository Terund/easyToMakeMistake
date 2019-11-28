class MyDecorator:
    function = []
    messages = []

    def __init__(self, func, msg="hello"):
        self.function.append(func)
        self.messages.append(msg)

    def inner(self, func):
        this_class = type(self)
        return this_class(func, msg="world")

    def __call__(self, *args, **kwargs):
        for i, func in enumerate(self.function):
            func(self.messages[i])


@MyDecorator
def first(a):
    print("first:", a)


@first.inner
def second(a):
    print("second:", a)


first()
second()
