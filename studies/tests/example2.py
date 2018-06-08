# -*- coding: utf-8 -*-
import sys
import logging

def test_print():
    print('Print to stdout')
    print('Print to stderr', file=sys.stderr)
    logging.debug('Print to debug')
    logging.info('Print to info')
    logging.warning('Print to warning')
    logging.error('Print to error')

test_print()
