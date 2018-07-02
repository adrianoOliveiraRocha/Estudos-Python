# -*- coding: utf-8 -*-

#def firstn(n):
#    num, nums = 0, []
#    while num < n:
#        nums.append(num)
#        num += 1
#    return nums
#
#sum_of_first_n = sum(firstn(1000000))
#
#print(sum_of_first_n)
#

class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []
        
    def __iter__(self):
        return self
        
    def __next__(self):
        return self.next()
        
    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        else:
            raise StopIteration()
            

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)


#now, we gonna do it with generator
def firstn(n):
    while num < n:
        yield num
        num += 1
        
