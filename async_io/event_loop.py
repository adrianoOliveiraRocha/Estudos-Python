# -*- coding: utf-8 -*-
import time
import asyncio


t = time.time()

def printer(name):
    print('Start %s at %.1f' % (name, time.time() - t))
    time.sleep(0.2)
    print('Finished %s at %.1f' % (name, time.time() - t))
    print('\n')

loop = asyncio.get_event_loop()

# Call a function at a specific time related to the output of loop.time .
# Every integer after loop.time adds a second
result = loop.call_at(loop.time() + .2, printer, 'call_at')

# Call the function after the given number of seconds
result = loop.call_later(.1, printer, 'call_later')

# Add an item to the end of the (FIFO) queue
result = loop.call_soon(printer, 'call_soon')

# This is the same as call_soon except for being
# thread safe
result = loop.call_soon_threadsafe(printer, 'call_soon_threadsafe')
# Make sure we stop after a second
result = loop.call_later(1, loop.stop)

loop.run_forever()


