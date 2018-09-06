# -*- coding: utf-8 -*-
import re

try:
    resp = re.search(r'number [0-6]', 'number 7').group()
    print(resp)
except Exception as e:
    print(e)