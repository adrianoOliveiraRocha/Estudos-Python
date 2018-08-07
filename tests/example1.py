# -*- coding: utf-8 -*-
import unittest


class Calc(object):
    def _sum(self, x, y):
        return x + y
    
    def subtraction(self, x, y):
        return x - y
    
    def multplication(self, x, y):
        return x * y
        
    def division(self, x, y):
        return x/y


class CalcTest(unittest.TestCase):
    
    def test_sum(self):
        calc = Calc()
        self.assertEqual(calc._sum(2, 2), 4)
        
    def test_subtraction(self):
        calc = Calc()
        self.assertEqual(calc.subtraction(2, 2), 0)
        
    def test_multplication(self):
        calc = Calc()
        self.assertEqual(calc.multplication(2, 2), 4)
        
    def test_division(self):
        calc = Calc()
        self.assertEqual(calc.division(2, 2), 1)
    

if __name__ == '__main__':
    unittest.main()

