# -*- coding: utf-8 -*-
import sys 
import pstats
import profile
import functools


@functools.lru_cache()
def fibonacci_cached(n):
    if n < 2:
        return n
    else:
        return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)
        

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        

if __name__ == '__main__':
    profiler = profile.Profile(bias=2.0939406059394783e-06)
    n = 30
    
    if sys.argv[-1] == 'cache':
        profiler.runcall(fibonacci_cached, n)
    else:
        profiler.runcall(fibonacci, n)
    stats = pstats.Stats(profiler).sort_stats('calls')
    stats.print_stats()
     
# python3 test_fibonacci3.py no_cache

