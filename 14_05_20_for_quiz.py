# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:42:27 2020

@author: marco
"""
    #       it = html_str + items[0] + html_str
items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)