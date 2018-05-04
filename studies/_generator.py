# -*- coding: utf-8 -*-

def count(start=0, step=1, stop=10):
    n = start
    while n <= stop:
        yield n
        n += step

for x in count(10, 2.5, 20):
    print(x)

# example 1
class Count(object):
    def __init__(self, start=0, step=1, stop=10):
        self.n = start
        self.step = step
        self.stop = stop
    
    def __iter__(self):
        return self
        
    def __next__(self):
        n = self.n
        if n > self.stop:
            raise StopIteration()
        self.n += self.step
        return n

for x in Count(10, 2.5, 20):
    print(x)
# example 2    
def generator():
    """This example show that the statement is freeze. It is lazy"""
    print('Before 1')
    yield 1
    print('After 1')
    print('Before 2')
    yield 2
    print('After 2')
    print('Before 3')
    yield 3

g = generator()

print('Got %d' % next(g))
print('Got %d' % next(g))
print('Got %d' % next(g))
