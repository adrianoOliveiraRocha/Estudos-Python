# -*- coding: utf-8 -*-
import datetime
import multiprocessing


def busy_wait(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    n = 10000000
    start = datetime.datetime.now()
    
    processes = []
    for _ in range(5): # my computer have 5 cores
        process = multiprocessing.Process(
                    target=busy_wait, args=(n,))
        process.start()
        processes.append(process)
    
    for process in processes:
        process.join()
        
    end = datetime.datetime.now()
    print("The multiprocessed loops took: %s" % (end - start))
    # The multiprocessed loops took: 0:00:01.043420
   