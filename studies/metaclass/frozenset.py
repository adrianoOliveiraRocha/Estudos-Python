# -*- coding: utf-8 -*-


class AbstractMeta(type):
    def __new__(metaclass, name, bases, namespace):
        cls = super().__new__(metaclass, name, bases, namespace)
        cls.__abstractmethods__ = frozenset(('something', ))
        return cls


class Spam(metaclass=AbstractMeta):
    pass


try:
    eggs = Spam()
except TypeError as te:
    print(te)
    '''Can't instantiate abstract class Spam 
    with abstract methods something'''