# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:00:02 2020

@author: marco
"""
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0
for tk in tokens:
    if tk.startswith("<") and tk.endswith(">"):
       count += 1
print(count)
