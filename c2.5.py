#!/usr/bin/env python3

text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

import re

new_text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text)
print(new_text)

