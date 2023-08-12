from abc import ABC,ABCMeta

class MyClass(ABC):
    pass

obj=MyClass()
print(type(ABC))

class MyABC(metaclass=ABCMeta):
    pass

MyClass.register(tuple)
assert issubclass(tuple,MyClass)
