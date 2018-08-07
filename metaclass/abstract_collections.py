# -*- coding: utf-8 -*-
import abc


class Spam(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def some_method(self):
        raise NotImplemented()
    
    
class Eggs(Spam):
    def some_new_method(self):
        pass
    

try:
    eggs = Eggs()
except TypeError as error:
    print(error)


class Bacon(Spam):
    def some_method():
        pass


bacon = Bacon()   
print(bacon)     


class Spam(object, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def some_property(self):
        raise NotImplemented()
    
    @classmethod
    @abc.abstractmethod
    def some_classmethod(cls):
        raise NotImplemented
        
    @staticmethod
    @abc.abstractmethod
    def some_staticmethod():
        raise NotImplemented

    @abc.abstractmethod
    def some_method():
        raise NotImplemented        
        
    
    
