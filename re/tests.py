# -*- coding: utf-8 -*-
import re

heading  = r'<h1>TITLE</h1>'
print(re.match(r'<.*>', heading).group())

# https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial?utm_source=adwords_ppc
