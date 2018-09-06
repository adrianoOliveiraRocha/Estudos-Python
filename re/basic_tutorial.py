# -*- coding: utf-8 -*-
import re

# Basic Patterns: Ordinary Characters
if re.match(r'Python', 'Python Programmer'):
    print('Match!')
else:
    print('Not a match')

# Wild Card Characters: Special Characters
# . - You can use it when you don't know which letter exists in this position
re.search(r'P.thon Program.er', 'Python Programmer').group()

# \w - Lowercase w. Matches any single letter, digit or underscore.
re.search(r'P\wthon Program.er', 'Python Programmer').group()

# \W - Uppercase w. Matches any character not part of \w (lowercase w)
re.search(r'P\Wthon Program.er', 'P@thon Programmer').group()

# \s - Lowercase s. Matches a single whitespace character like: space, newline, tab, return
re.search(r'Python\sProgrammer', 'Python Programmer').group()

# \S - Uppercase s. Matches any character not part of \s (lowercase s)
re.search(r'Python Programm\Sr', 'Python Programmer').group()

# \t - Lowercase t. Matches tab
re.search(r'Python\tProgrammer', 'Python    Programmer').group()

# \t - Lowercase t. Matches tab
re.search(r'Python\tProgrammer', 'Python    Programmer').group()

# \n - Lowercase n. Matches newline
# \r - Lowercase r. Matches return
# \d - Lowercase d. Matches decimal digit 0-9
re.search(r'Py\dho\d Programmer', 'Py1ho3 Programmer').group()

# ^ - Caret. Matches a pattern at the start of the string
re.search(r'^Python', 'Python Programmer').group()

# $ - Matches a pattern at the end of string
re.search(r'Programmer$', 'Python Programmer').group()

# [abc] - Matches a or b or c
re.search(r'Python Program[mrf]er', 'Python Programmer').group()

# [a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9).
# Characters that are not within a range can be matched by complementing
# the set. If the first character of the set is ^, all the characters that
# are not in the set will be matched
re.search(r'number [0-6]', 'number 5').group()

# https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial?utm_source=adwords_ppc