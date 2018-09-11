# -*- coding: utf-8 -*-
import re

# Basic Patterns: Ordinary Characters
if re.match(r'Python', 'Python Programmer'):
    print('Match!')
else:
    print('Not a match')

# Wild Card Characters: Special Characters
# \. - You can use it when you don't know which letter exists in this position
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

# Matches any character except 5
re.search(r'Number: [^5]', 'Number: 0').group()

# \A - Uppercase a. Matches only at the start of the string. Works across multiple lines as well
re.search(r'\A[A-E]ookie', 'Cookie').group()

"""
\ - Backslash. If the character following the backslash is a recognized escape
character, then the special meaning of the term is taken. For example,
\n is considered as newline. However, if the character following the \
is not a recognized escape character, then the \ is treated like any other
character and passed through.
"""

# This checks for '\' in the string instead of '\t' due to the '\' used
re.search(r'Back\\stail', 'Back\stail').group()

# This treats '\s' as an escape character because it lacks '\' at the start of '\s'
re.search(r'Back\stail', 'Back tail').group()

# + - Checks for one or more characters to its left
re.search(r'Co+kie', 'Cooookie').group()

# * - Checks for zero or more characters to its left
re.search(r'Ca*o*kie', 'Caokie').group()

# ? - Checks for exactly zero or one character to its left.
re.search(r'Colou?r', 'Color').group()

# {x} - Repeat exactly x number of times.
# {x,} - Repeat at least x times or more
# {x, y} - Repeat at least x times but no more than y times
re.search(r'\d{9,10}', '0987654321').group()

# Example email
email_address = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', email_address)

if email_address:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
