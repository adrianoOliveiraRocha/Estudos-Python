# -*- coding: utf-8 -*-


class Meta(type):
    
    @property
    def spam(cls):
        return 'Spam property of %r' % cls
        
    def eggs(self):
        return 'Eggs method of %r' % self
    

class SomeClass(metaclass=Meta):
    pass


print(SomeClass.spam)
print(SomeClass.eggs())

try: 
    print(SomeClass().spam)
except AttributeError as error:
    print(error)

try: 
    print(SomeClass().eggs())
except AttributeError as error:
    print(error)